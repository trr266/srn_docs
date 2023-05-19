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

Currently our data covers 8,988 documents from 713 firms spanning 17
countries and data from the time period 2010 to 2022. Further
information on the covered firm-years can be assessed from the table
below.

| Country        | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|:---------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
| Austria        |    7 |    7 |    7 |    7 |    7 |    7 |    8 |    8 |    8 |    8 |    8 |      |    4 |
| Belgium        |   10 |   10 |   11 |   11 |   12 |   12 |   16 |   14 |   15 |   16 |   14 |    2 |    7 |
| Denmark        |   13 |   14 |   14 |   14 |   14 |   17 |   19 |   19 |   20 |   20 |   20 |    4 |   12 |
| Finland        |   10 |    9 |   10 |   11 |   11 |   12 |   14 |   15 |   15 |   15 |   16 |    2 |    9 |
| France         |   45 |   48 |   53 |   52 |   56 |   59 |   68 |   68 |   70 |   73 |   71 |   25 |   56 |
| Germany        |   45 |   44 |   44 |   43 |   48 |   49 |   63 |   65 |   68 |   68 |   70 |  164 |  140 |
| Ireland        |    5 |    5 |    5 |    4 |    5 |    6 |    7 |    7 |    7 |    7 |    7 |    4 |    7 |
| Italy          |   14 |   18 |   20 |   22 |   22 |   23 |   27 |   27 |   27 |   27 |   28 |    8 |   15 |
| Netherlands    |   14 |   16 |   17 |   18 |   23 |   22 |   27 |   26 |   28 |   30 |   32 |    9 |   25 |
| Norway         |   12 |   13 |   13 |   15 |   15 |   15 |   16 |   16 |   16 |   17 |   17 |    4 |   13 |
| Poland         |    1 |    2 |    2 |    3 |    4 |    4 |    6 |    6 |    6 |    6 |    7 |      |    2 |
| Portugal       |    2 |    2 |    3 |    3 |    3 |    3 |    4 |    4 |    4 |    4 |    4 |    1 |    2 |
| Russia         |    1 |      |      |      |      |      |      |      |      |      |      |      |      |
| Spain          |   13 |   17 |   18 |   21 |   22 |   22 |   25 |   25 |   25 |   25 |   24 |    7 |   12 |
| Sweden         |   45 |   44 |   47 |   50 |   52 |   55 |   58 |   62 |   62 |   62 |   62 |    7 |   35 |
| Switzerland    |   33 |   35 |   36 |   37 |   39 |   40 |   49 |   50 |   50 |   52 |   51 |    8 |   20 |
| United Kingdom |   98 |  101 |  100 |  104 |  107 |  115 |  128 |  129 |  135 |  137 |  137 |   14 |   78 |

### Included report types

We try to collect all documents that contain relevant sustainability
information. This includes but is not limited to annual and
sustainability reports (AR and SR). For some firms it also includes
additional reports like integreated reports (IR), Carbon Diclosure
Project data (CDP) and other reporting formats. All materials are
referred to by URL links and are provided as is. Neither the team of the
SRN nor the maintainers of this data repository claim any ownership of
or legal rights to the provided data.

| Country        | \# Firms |   AR |  SR |  IR | CDP |  AR | AR_SR |  GR | Other |
|:---------------|---------:|-----:|----:|----:|----:|----:|------:|----:|------:|
| Austria        |        8 |   74 |  42 |   0 |   0 |   0 |     0 |   0 |    15 |
| Belgium        |       18 |  137 |  49 |   1 |   0 |   0 |     0 |   0 |     5 |
| Denmark        |       21 |  158 | 150 |   4 |   0 |   0 |     0 |  11 |    55 |
| Finland        |       17 |  135 |  72 |   1 |   0 |   0 |     0 |   6 |    58 |
| France         |       77 |  542 | 360 |  47 |   1 |   0 |     0 |   1 |    26 |
| Germany        |      171 |  805 | 579 |  35 |   3 |   0 |     0 |   9 |    47 |
| Ireland        |        8 |   73 |  34 |   0 |   1 |   0 |     0 |   0 |     3 |
| Italy          |       30 |  234 | 196 |  10 |   0 |   0 |     0 |   3 |    58 |
| Netherlands    |       35 |  198 | 153 |  16 |   0 |   0 |     0 |   0 |     8 |
| Norway         |       18 |  138 | 109 |   4 |   0 |   0 |     0 |   0 |     1 |
| Poland         |        8 |   25 |  22 |   0 |   0 |   0 |     0 |   1 |     8 |
| Portugal       |        4 |   35 |  17 |   1 |   0 |   0 |     0 |   0 |     7 |
| Russia         |        1 |    1 |   0 |   0 |   0 |   0 |     0 |   0 |     0 |
| Spain          |       25 |  176 | 191 |  12 |   0 |   0 |     0 |  16 |    84 |
| Sweden         |       68 |  533 | 299 |  28 |   2 |   8 |     1 |  24 |   154 |
| Switzerland    |       53 |  433 | 236 |  12 |   0 |   0 |     0 |  12 |    41 |
| United Kingdom |      151 | 1153 | 719 |  41 |   1 |   2 |     0 |   4 |    22 |

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
