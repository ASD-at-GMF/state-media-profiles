# State Media Profiles
This repository aims to provide a relatively comprehensive data set of state-affiliated media [fully qualified domain names](https://en.wikipedia.org/wiki/Fully_qualified_domain_name), when available or accessible, direct links to their social media profiles for use in media and information research. 

**It is crucial to note that nmot all 'state-affiliations' are made equal. A media outlet with funding, management, and editorial indepedence is not equivalent and should not be directly compared with those without. For example, in the United States, NPR is wholly independent in all three categories, while Voice of America is funded and managed by the US government, though not controlled editorially.**

## Acknowledgements and Contributions
The seed data (Country, Media Company, Main Assets, and Typology) were provided by the [State Media Monitor](https://statemediamonitor.com), a project of the [Media and Journalism Research Center](https://journalismresearch.org/).

This project was substantially contributed to by the following individuals:
- Ayleen Cameron, Alliance for Securing Democracy, acameron (at) gmfus.org
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

#### Caveats
Notable exclusions from this data:en
- Content delivery networks (cdns) - many sites use subdomains or other websites to deliver images, video, and other non-textual content to their website. e.g. **https://cdn-storage-media.tass.ru/**resize/108x72/tass_media/2023/08/10/i/1691696921773674_i_n8o-f8.jpg
- Test and mobile subdomains - many sites will use seperate subdomains (e.g. **m.**example.com) for their mobile site or surface content from their test or beta sites, like **https://test.exaample.com**

Notable choices for inclusion
- Mirror sites with similar registration information. Mirror sites typically cant't be proven to belong to a given entity 

## Sourcing 
