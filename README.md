# Sustainability Reporting Navigator Document Database

This repository features the document data and API of the [Sustainabity
Reporting Navigator](https://www.sustainabilityreportingnavigator.com).
The large bulk of the initial reports in our database comes from the
generous contribution by Arianna Pisciella, Gaia Melloni, Bianca Minuth,
and Paul Pronobis and is supplemented by the ongoing data collection of
the SRN team. Our objective is to develop this repository into a
collaborative data platform that provides extensive coverage of
sustainability-related documents published by European publicly-listed
firms.

### Coverage

Currently our data covers 1,109 documents from 468 firms spanning 16
countries and data from the time period 2021 to 2022. Further
information on the covered firm-years can be assessed from the table
below.

| Country        | 2021 | 2022 |
|:---------------|-----:|-----:|
| Austria        |      |    4 |
| Belgium        |    2 |    7 |
| Denmark        |    4 |   12 |
| Finland        |    2 |    9 |
| France         |   24 |   56 |
| Germany        |  164 |  142 |
| Ireland        |    4 |    7 |
| Italy          |    7 |   14 |
| Netherlands    |   10 |   25 |
| Norway         |    4 |   13 |
| Poland         |      |    2 |
| Portugal       |    1 |    2 |
| Spain          |    7 |   12 |
| Sweden         |    7 |   35 |
| Switzerland    |    8 |   20 |
| United Kingdom |   14 |   77 |

### Included report types

We try to collect all documents that contain relevant sustainability
information. This includes but is not limited to annual and
sustainability reports (AR and SR). For some firms it also includes
additional reports like integreated reports (IR), Carbon Diclosure
Project data (CDP) and other reporting formats. All materials are
referred to by URL links and are provided as is. Neither the team of the
SRN nor the maintainers of this data repository claim any ownership of
or legal rights to the provided data.

| Country        | \# Firms |  AR |  SR |  IR | CDP | Other |
|:---------------|---------:|----:|----:|----:|----:|------:|
| Austria        |        4 |   1 |   3 |   0 |   0 |     1 |
| Belgium        |        7 |   9 |   5 |   1 |   0 |     0 |
| Denmark        |       12 |  15 |  10 |   4 |   0 |     0 |
| Finland        |       10 |   9 |   5 |   0 |   0 |     2 |
| France         |       56 |  80 |  20 |   5 |   1 |     4 |
| Germany        |      170 | 289 | 199 |  27 |   3 |     7 |
| Ireland        |        7 |  10 |  10 |   0 |   1 |     0 |
| Italy          |       14 |  19 |  10 |   1 |   0 |     2 |
| Netherlands    |       25 |  36 |   6 |   1 |   0 |     6 |
| Norway         |       13 |  17 |   7 |   0 |   0 |     0 |
| Poland         |        2 |   1 |   1 |   0 |   0 |     0 |
| Portugal       |        2 |   3 |   1 |   0 |   0 |     1 |
| Spain          |       12 |  18 |   7 |   5 |   0 |     0 |
| Sweden         |       35 |  43 |  13 |   1 |   2 |     1 |
| Switzerland    |       22 |  22 |  22 |   2 |   0 |     2 |
| United Kingdom |       77 |  87 |  34 |   8 |   2 |     7 |

### How can I download the data?

We provide an easy to use API for data download. See the file
`srn_docs_api.py` in this repo for pointers. We are working on making
this process even easier to handle over the next weeks. Stay tuned!

### How do I cite the data?

Thank you for asking! We very much appreciate you giving credit to our
data collection efforts. We will be using a concept DOI and versioned
DOIs from Zenodo in the future. Currently, please cite the data as
follows:

Donau, Charlotte-Louise, Fikir Worku Edossa, Joachim Gassen, Gaia
Melloni, Inga Meringdal, Bianca Minuth, Arianna Piscella, Paul Pronobis
and Victor Wagner (2023): SRN Document Database,
https://github.com/trr266/srn_docs.

### How can I post-process the data?

What a great question! We really hope that this repo will be used to
discuss data quality issues as well as methods to use the data in
research projects. Again, as a first teaser, take a look at
`extraxt_text_from_docs.py` that features a method to extract page-wise
text data from our documents.

### I think I found something odd in the data. Whom should I contact?

Thank you! Please open an issue on GitHub, mentioning the document id
and describing the issue that you encountered.

### This is great! Can I help?

Thank you and yes, of course! We would be very happy about people that
provide historical data and/or are willing to maintain our data going
forward on a country or index basis. So, if you would like to help,
please reach out to [Victor Wagner](victor.wagner@lmu.de).
