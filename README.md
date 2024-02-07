# State Media Profiles
This repository aims to provide a relatively comprehensive data set of state-affiliated media [fully qualified domain names](https://en.wikipedia.org/wiki/Fully_qualified_domain_name), when available or accessible, direct links to their social media profiles for use in media and information research. 

**It is crucial to note that not all 'state-affiliations' are made equal. A media outlet with funding, management, and editorial indepedence is not equivalent and should not be directly compared with those without. For example, in the United States, NPR is wholly independent in all three categories, while Voice of America is funded and managed by the US government, though not controlled editorially.**

## Acknowledgements and Contributions
The seed data (Country, Media Company, Main Assets, and Typology) were provided by the [State Media Monitor](https://statemediamonitor.com), a project of the [Media and Journalism Research Center](https://journalismresearch.org/).

This project was substantially contributed to by the following individuals:
- Ayleen Cameron, Alliance for Securing Democracy, acameron (at) gmfus.org
- Gabriele Sava, Alliance for Securing Democracy
- Fabienne Aleth, Alliance for Securing Democracy
- Bret Schafer, Alliance for Securing Democracy, bschafer (at) gmfus.org
- Peter Benzoni, Alliance for Securing Democracy, pbenzoni (at) gmfus.org

If you'd like to contribute, please submit a pull request or contact Peter at pbenzoni (at) gmfus.org

## Methodology
This project inherits [the methodology of the State Media Monitor](https://statemediamonitor.com/methodology/) to define the criteria for inclusion and [typology](https://statemediamonitor.com/typology/).

### Critieria for inclusion
A given media outlet must have provable links to a state's government (typically, the minimum bar is funding them, though mechanisms vary) or fulfill one or more of the following criteria:
- State directly controls funding 
- State control of governing structures and ownership
- State control of the editorial process
  
For detailed defintions and thresholds for inclusion, please refer to [the methodology of the State Media Monitor](https://statemediamonitor.com/methodology/).

### Typology
It's highly suggested to read the [State Media Monitor's full typology](https://statemediamonitor.com/typology/) to understand the justification and nuances of how state-affiliated media function

|Direct funding control|Control of governing structures and ownership|Editorial control|Model|Code|
|-----|---------|------|------|------|
|Yes|Yes|Yes|State-controlled media|SC|
|No|Yes|Yes|Captured public/state-managed media|CaPu|
|Yes/No|No|Yes|Captured private media|CaPr}
|Yes|Yes|No|Independent state-funded and state-managed media|ISFM|
|Yes|No|No|Independent state-funded media|ISF|
|No|Yes|No|Independent state-managed media|ISM|
|No|No|No|Independent public media|IP|

## Data

### Website Data 
This data aims to be comprehensive, not exhaustive and is aimed at finding fully qualified domain names where a reasonable user could encounter relevant content or find more inforation about the media asset. In practice, this means a few sites may have minimal or no 'media' content but are included e cause they host information about, for example, the set of redio stations they administer. 
>**Definition: Fully Qualified Domain Name**
> 
> A fully qualified domain name (FQDN) is the complete address of an internet host or computer. It consists of the subdomain, domain name, and top-level domain (TLD). For example, an FQDN in the data is arabic.people.com.cn, which breaks down into a subdomain of 'arabic', a domain of 'people' and a TLD of 'com.cn'
If any of these (subdomain, domain name, or top-level domain) is different, even in the same organization, a new entry is merited. For example, www.bbc.com vs www.bbc.co.uk or espanol.cgtn.com vs francais.cgtn.com 

#### Caveats
Notable exclusions from this data:
- Content delivery networks (cdns) - many sites use subdomains or other websites to deliver images, video, and other non-textual content to their website. e.g. **cdn-storage-media.tass.ru/**
- Test and mobile subdomains - many sites will use seperate subdomains (e.g. **m.**example.com) for their mobile site or surface content from their test or beta sites, like **test.example.com**
- Any other subdomain unlikely to be encountered during normal use, including rss feeds, mail servers, authentication, intranets, etc.

Notable choices for inclusion
- Mirror sites with similar registration information. Mirror sites typically cant't be proven to belong to a given entity, but in cases where they are, inclusion of mirror sites is acceptable. A good example of this is swentr.site, which is registered to the same entity as rt.com, ANO TV-Novosti
- 'Duplicate' sites, with a shared parent organization. A good example of this is Spain's [Canal Sur](https://www.canalsur.es/), which runs both television and radio services.

### Social Media URLs
When known and available, links to the social media profiles of each state media entry is provided for the following sites:
- Instagram
- Twitter
- Facebook
- Youtube
- Telegram
- VK
- Linkedin
- Ok.ru
- Tiktok
- Rutube
- Other streaming media 

This data was primarily sourced from WikiData and manual classification. 

## Sourcing 
All data not in these columns (Country, Media Company, Main Assets, and Typology) was manually entered and reviewed by a human, and is therefore prone to mistakes or omissions. If you think something was missed or is incorrect please submit a pull request or contact Peter at pbenzoni (at) gmfus.org.
As mentioned, the seed data for this project was provided by the [State Media Monitor](https://statemediamonitor.com). Substantial addititional contributions were also sourced from projects from the [Alliance for Securing Democracy.](https://securingdemocracy.gmfus.org/)

## Using the RSS parser
1. Create a file, config.py in the root of the repository and provide the following, each on a line: DB_FILE, (leave this empty, used to be a path to a sqllite database ) MEDIA_FILE, (a link to the State Media Excel file) SOURCE_TYPE, (either 'database' or 'excel', indicating where to source its list of rss feeds)  POSTGRES_STRING (a valid postgres database string, e.g 'postgresql://username:USER-PASSWORD@path.to.hosted.database.service:26257/database?sslmode=verify-full'
2. ```pip install traceback lxml psycopg2 concurrent pandas nltk sqlite3 newspaper3k feedparser```
3. run the file in your execution environment of choice

## Contributor Organizations
Click the logo to be directed to the contributor site
\
\
[<img src="https://securingdemocracy.gmfus.org/wp-content/uploads/2023/08/MJRC-Logo-FT-1.png" alt="MJRC Logo" height="256"/>](https://journalismresearch.org/) [<img src="https://securingdemocracy.gmfus.org/wp-content/uploads/2023/08/cropped-asd-social-icon-w-bg-01.png" alt="ASD Logo" height="256" />
](https://securingdemocracy.gmfus.org/)
