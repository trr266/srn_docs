## Sustainability Reporting Navigator Document Database

This repository features the dcoument data and API of the 
[Sustainabity Reporting Navigator](https://www.sustainabilityreportingnavigator.com).
Starting from the data collection efforts by the SRN team as well as 
inpedendent data collection by Bianca Minuth and Arianna Piscella, 
our objective is to develop it into a collaborative data platform that 
provides extensive coverage of sustainability-related documents published 
by European publicly-listed firms.


### Coverage

Currently our data covers x,qyz firm spanning xyz countries and data from
the time period 20xx to 2022. Further information can be assessed from
the table below.

<dynamic table firm countries x year)>


### Included report types

We try to collect all documents that contain relevant sustainability 
information. This includes but is not limited to annual and sustainability
reports. For some firms it also includes andditional reports like governance 
reports or additional info. All materials have been collected from the firm 
websites and are provided as is. Neither the team of the SRN nor the maintainers 
of this data repository claim any ownership of or legal rights to own the 
provided data. 

<dynamic table report types>


### Document formats

Most of the documents are stored as PDFs but some are scraped HTML files or
other Formats (e.g., Excel or Word).


### How can I download the data?

We provide an easy to use API for data download. See the file `srn_docs_api.py` 
in this repo for pointers. We are working on making this process even easier 
to handle over the next weeks. Stay tuned!


### How do I cite the data?

Thank you for asking! We very much appreciate you giving credit to our data 
collection efforts. We will be using a concept DOI and verioned DOIs 
from Zenodo in the future. Currently please cite the data as follows:

Minuth, Bianca; Piscella, Arianna, and Wagner, Victor (2023): SRN Document 
Data, https://github.com/trr266/srn_docs.


### How can I post-process the data?

What a great question! We really hope that this repo will be used to discuss 
and exchange data quality issues as well as methods to use the data in research
project. Again, as a first teaser, take a look at 
`extraxt_text_from_docs.py` that features a method to extract page-wise 
text data from our documents.


### I think I found something odd in the data. Whom should I contact.

Thank you! Please consider open an issue on GitHub, mentioning the document id 
and describing the issue that you encounter.


### This is great! Can I help?

Thank you and yes, of course! We would be very happy about people that 
provide historical data and/or are willing to maintain our data going 
forward on a country or index basis. So, if you would like to help, please
reach out to Victor Wagner. 


### To do/discuss

- [ ] Separate the publicly accessible API endpoints from an internal SRN API?
- [ ] Do we need to use API keys (preregistration required)?
- [ ] Include in metadata documents: contributer, document_format
- [ ] Include in metadata firms: maintainer, LEI, main URL and IR URL?
- [ ] Standardize firm names a little bit better (legal form?)
- [ ] What's wrong with stale downloads (e.g. BMW)
- [ ] The HTML files are mostly not really usable (no following through on links, 404)
- [ ] Create versioned data structure that allows reproducible downloads via timestamp


### Ideas for later

- [ ] Package this into python and R packages
- [ ] Provice curate tools for pre-processing the data
- [ ] Develop API/Webforms for uploading contributed data and metadata
- [ ] Develop tools for data maintainers (web scrapers with alarm feature)



