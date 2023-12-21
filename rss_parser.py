import feedparser
from newspaper import Article
import sqlite3
import datetime
import nltk
import pandas as pd
import dateutil.parser
import pytz
from concurrent.futures import ThreadPoolExecutor, as_completed
import psycopg2
from lxml.etree import tostring
import lxml
import traceback

utc=pytz.UTC

from config import DB_FILE, MEDIA_FILE, SOURCE_TYPE, POSTGRES_STRING
nltk.download('punkt')

def make_aware(dt, timezone=pytz.utc):
    """Convert offset-naive datetime to offset-aware using the given timezone."""
    return dt if dt.tzinfo else timezone.localize(dt)
        
def extract_embedded_links(article_clean_top_node):
    # Find all URLs in the HTML content
    urls = article_clean_top_node.xpath("//a/@href")

    return urls

def extract_tweet_details(article_clean_top_node):
    # Find all embedded tweets using the appropriate class name
    embedded_tweets = article_clean_top_node.xpath(".//blockquote[contains(@class, 'twitter-tweet')]")

    tweets_data = []

    for tweet in embedded_tweets:
        tweet_data = {}

        # The tweet URL is typically contained within the last <a> tag in the blockquote.
        tweet_link = tweet.xpath(".//a/@href")[-1] if tweet.xpath(".//a/@href") else None
        if tweet_link:
            tweet_data['tweetLink'] = tweet_link
            
            # Extract tweet ID from the tweet URL
            tweet_data['tweetId'] = tweet_link.split('/')[-1]
            
            # Extract the screen name from the tweet URL
            parts = tweet_link.split('/')
            tweet_data['screenName'] = parts[-3] if len(parts) > 3 else None

        # The full text of the tweet is contained in the <p> tag within the blockquote
        tweet_text_list = tweet.xpath(".//p//text()")
        tweet_data['tweetText'] = ''.join(tweet_text_list).strip() if tweet_text_list else None

        tweets_data.append(tweet_data)

    return tweets_data


# Function to parse and display each feed
def process_and_insert(cursor, known_urls, source, feedName, url, country):
    feed = feedparser.parse(url)
    print(len(feed.entries), feedName, url)
        # Create a new connection for each thread
    with psycopg2.connect(POSTGRES_STRING) as conn:
        cursor = conn.cursor()

        for entry in feed.entries:
            if 'link' not in entry or 'published' not in entry:
                continue
            elif entry.link in known_urls or  make_aware(dateutil.parser.parse(entry.published)) < make_aware(datetime.datetime.now() - datetime.timedelta(days=2)):
                continue       
            try:
                # Use Newspaper3k to extract details
                article = Article(entry.link)
                article.download()
                article.parse()
                article.nlp()
                
                # Extracting the fields for the output table
                author = ', '.join(article.authors)
                country = country
                createdAt = datetime.datetime.now()
                excerpt = article.text
                language = article.meta_lang
                outlet = source
                publishedDate = article.publish_date or entry.published
                siteCountry = ''  # This needs to be determined possibly from the URL or another source
                title = article.title
                url = entry.link
                websiteName = feedName
                featuredImage = article.top_image # new field
                # Add description?

                # Insert data into the output table
                # Insert data into the articles table
                cursor.execute('''
                INSERT INTO public.articles (
                    author,
                    country,
                    createdAt,
                    excerpt,
                    language,
                    outlet,
                    publishedDate,
                    siteCountry,
                    title,
                    url,
                    websiteName,
                    featuredImage
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING articleId
                ''', (author, country, createdAt, excerpt, language, outlet, publishedDate, siteCountry, title, url, websiteName, featuredImage))
                conn.commit()
                # Retrieve the last inserted article_id
                this_article_id = cursor.fetchone()[0]

                if hasattr(article, 'tags' ) and len(article.tags) > 0:
                    # Insert an entry for each tag in article.tags
                    tag_data = [(this_article_id, tag) for tag in article.tags]
                    cursor.executemany('''
                        INSERT INTO public.tags (article_id, tag) VALUES (%s, %s)
                    ''', tag_data)
                if hasattr(article,'keywords') and len(article.keywords) > 0:
                    # Insert an entry for each keyword in article.keywords
                    keyword_data = [(this_article_id, keyword) for keyword in article.keywords]
                    cursor.executemany('''
                        INSERT INTO public.keywords (article_id, keyword) VALUES (%s, %s)
                    ''', keyword_data)
                
                conn.commit()
                # Assuming article.clean_top_node contains the necessary data
                if article.clean_top_node is not None:
                    all_urls = extract_embedded_links(article.clean_top_node)
                    embedded_tweets = extract_tweet_details(article.clean_top_node)
                    if len(embedded_tweets) > 0:
                        tweet_data = [(this_article_id, tweet['tweetLink'], tweet['tweetId'], tweet['screenName'], tweet['tweetText']) for tweet in embedded_tweets]
                        cursor.executemany('''
                            INSERT INTO public.tweets (article_id, tweetLink, tweetId, screenName, tweetText) VALUES (%s, %s, %s, %s, %s)
                        ''', tweet_data)
                    if len(all_urls) > 0:
                        url_data = [(this_article_id, url) for url in all_urls]
                        cursor.executemany('''
                            INSERT INTO public.urls (article_id, url) VALUES (%s, %s)
                        ''', url_data)

            except Exception as e:
                print(e, traceback.format_exc())
                print(url, ' | Error processing article: ', entry)
                continue
            finally:
                # Make sure to commit any changes
                conn.commit()
            

    print('Done processing feed: ', url, feedName)

def process_feed(data, known_urls):
    source, feedName, url, country = data

    # Call the original process_and_insert function
    process_and_insert(cursor, known_urls, source, feedName, url, country)


with psycopg2.connect(POSTGRES_STRING) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM articles")
    known_urls = cursor.fetchall()

    if SOURCE_TYPE == 'database':
        # Retrieve the RSS feed data from the database
        cursor.execute("SELECT source, title, url, country FROM rss_feeds")
        rows = cursor.fetchall()
        for row in rows:
            process_feed(row, known_urls) 

    else:
        # Retrieve the RSS feed data from the CSV file
        media_df = pd.read_excel(MEDIA_FILE, sheet_name='State_Media_Matrix')
        #split rss feeds into separate rows by comma without using assign

        #drop rows without rss feeds
        media_df = media_df.dropna(subset=['RSS Feeds'])

        media_df['RSS Feeds'] = media_df['RSS Feeds'].str.split(',')
        media_df = media_df.explode('RSS Feeds')
        
        #drop rows with with '' in rss feeds
        media_df = media_df[media_df['RSS Feeds']!='']

        media_df = media_df[media_df['Tracked']==1]

        # # insert rss feeds into database
        # for index,row in media_df.iterrows():
        #     cursor.execute('''
        #     INSERT INTO rss_feeds (
        #         source,
        #         title,
        #         url,
        #         country
        #     ) VALUES (?, ?, ?, ?)
        #     ''', (row['Media company'], row['Main assets'], row['RSS Feeds'], row['Country'])) 

        feed_data = [(row['Media company'], row['Main assets'], row['RSS Feeds'], row['Country']) for index, row in media_df.iterrows()]

        for feed in feed_data:
            process_feed(feed, known_urls) 