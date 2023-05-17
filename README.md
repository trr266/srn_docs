```{python}
#| echo: false
#| output: false

from srn_docs_api import get_srn_companies, get_srn_documents
import pandas as pd

SRN_API_URL = "https://api.sustainabilityreportingnavigator.com/api/"

def prep_table():
    companies = pd.DataFrame(get_srn_companies(SRN_API_URL))
    documents = pd.DataFrame(get_srn_documents(SRN_API_URL))
    df = documents.merge(companies, left_on='company_id', right_on='id')
    df = df[['country', 'type', 'year', 'company_id']]

    # table 1

    table_1 = df.groupby(['country', 'year']).agg(
        {'company_id': 'nunique'}).reset_index()

    # Pivot the table to have separate columns for the number of AR and SR
    table_1 = (table_1
               .pivot(index='country', columns='year', values='company_id')
               .reset_index()
               .fillna(''))

    table_1 = table_1.to_markdown(index=False)

    # table 2
    table_2 = pd.concat([df, pd.get_dummies(df['type'])], axis=1)
    aggregations = {}
    for col in table_2.columns[3:]:
        aggregations[col] = 'nunique' if col == 'company_id' else 'sum'
    table_2 = (table_2
               .drop('year', axis=1)
               .groupby('country')
               .agg(aggregations)
               .rename(columns={'company_id': 'number of firms'})
               .fillna(''))
    table_2 = table_2.to_markdown()

    return df, table_1, table_2
df, table_1, table_2 = prep_table()
```
## Sustainability Reporting Navigator Document Database

This repository features the document data and API of the 
[Sustainabity Reporting Navigator](https://www.sustainabilityreportingnavigator.com).
Starting from the data collection efforts by the SRN team as well as 
inpedendent data collection by Bianca Minuth and Arianna Piscella, 
our objective is to develop this repository into a collaborative data platform that 
provides extensive coverage of sustainability-related documents published 
by European publicly-listed firms.


### Coverage

```{python}
#| echo: false
#| output: asis
print(
f'''
Currently our data covers `{len(df.company_id.unique())}` firm spanning `{len(df.country.unique())}` countries and data from the time period `{df.year.min()}` to `{df.year.max()}`. Further information can be assessed from the table below.
'''
)
```

```{python}
#| echo: false
#| output: asis

print(table_1)
```

### Included report types

We try to collect all documents that contain relevant sustainability 
information. This includes but is not limited to annual and sustainability
reports. For some firms it also includes additional reports like governance 
reports or integrated reports. All materials have been collected from the firm 
websites and are provided as is. Neither the team of the SRN nor the maintainers 
of this data repository claim any ownership of or legal rights to the 
provided data. 

```{python}
#| echo: false
#| output: asis

print(table_2)
```


### How can I download the data?

We provide an easy to use API for data download. See the file `srn_docs_api.py` 
in this repo for pointers. We are working on making this process even easier 
to handle over the next weeks. Stay tuned!

### How do I cite the data?

Thank you for asking! We very much appreciate you giving credit to our data 
collection efforts. We will be using a concept DOI and versioned DOIs 
from Zenodo in the future. Currently, please cite the data as follows:

Minuth, Bianca, Arianna Piscella, Charlotte-Louise Donau, Inga Meringdal and Victor Wagner (2023): SRN Document 
Database, https://github.com/trr266/srn_docs.

### How can I post-process the data?

What a great question! We really hope that this repo will be used to discuss 
data quality issues as well as methods to use the data in research
projects. Again, as a first teaser, take a look at 
`extraxt_text_from_docs.py` that features a method to extract page-wise 
text data from our documents.


### I think I found something odd in the data. Whom should I contact?

Thank you! Please open an issue on GitHub, mentioning the document id 
and describing the issue that you encountered.


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



