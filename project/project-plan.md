# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing Greenhouse Gas Emissions, Air Pollutants, and Economic Sector Interplay in Germany

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Which industries emit the most air pollutants and greenhouse gases?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Greenhouse gases and air pollutants are major contributors to both climate change and air pollution, posing threats to essential aspects of human and ecosystem health. This project aims to provide insight into the industries in Germany responsible for the highest emissions and how these emissions have evolved over time. Therefore, it will examine the types of different greenhouse gases and air pollutants emitted by various sectors. The findings of this analysis will shed light on which industries present a substantial risk to air quality and contribute to warming trends in Germany.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

All the datasources are obtained from the Statistisches Bundesamt (Destatis), Deutschland.
License: Data licence Germany – attribution – Version 2.0, license text available at www.govdata.de/dl-de/by-2-0.			


### Datasource1: Air Emissions until 2019
* Metadata URL: https://www.govdata.de/ckan/dataset/luftemisions-deutschland-jahre-luftemissionsartproduktionsbereich.rdf
* Data URL: https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0001_00.csv
* Data Type: CSV

This dataset contains information about the types of gases emitted and the sectors responsible between 1995-2019.

### Datasource2: Air Emissions in 2020
* Data URL: [link to the data](https://www-genesis.destatis.de/datenbank/beta/statistic/85111/table/85111-0002/table-toolbar#filter=eyJoaWRlRW1wdHlDb2xzIjpmYWxzZSwiaGlkZUVtcHR5Um93cyI6ZmFsc2UsImNhcHRpb24iOlt7ImlkIjoiczEuODUxMTEiLCJ2YWx1ZXNJZHMiOlsiODUxMTEiXSwiY2hpbGRyZW4iOlt7ImlkIjoidjEuRElOU0ciLCJ2YWx1ZXNJZHMiOlsiREciXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJzaG93VmFyaWFibGUiOmZhbHNlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJzb3J0IjoiQ29kZUFzYyIsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjEiLCJibG9ja0lkIjoiMC4wIn1dLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InMxIiwiYmxvY2tJZCI6IjAifSx7ImlkIjoidjEuRElOU0ciLCJ2YWx1ZXNJZHMiOlsiREciXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJzaG93VmFyaWFibGUiOmZhbHNlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJzb3J0IjoiQ29kZUFzYyIsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjEiLCJibG9ja0lkIjoiMC4wIn1dLCJyb3dIZWFkZXIiOlt7ImlkIjoidjIuSkFIUiIsInZhbHVlc0lkcyI6WyIyMDIwIl0sImNoaWxkcmVuIjpbeyJpZCI6ImMxLkVNUzAwMSIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOlt7ImlkIjoidjQuV1owOFUxIiwidmFsdWVzSWRzIjpbIldaMDgtQSIsIldaMDgtMDEiLCJXWjA4LTAyIiwiV1owOC0wMyIsIldaMDgtQiIsIldaMDgtMDUiLCJXWjA4LTA2IiwiV1owOC0wNy0wMSIsIldaMDgtQyIsIldaMDgtMTAtMDMiLCJXWjA4LTEzLTA0IiwiV1owOC0xNiIsIldaMDgtMTciLCJXWjA4LTE4IiwiV1owOC0xOSIsIldaMDgtMTkxIiwiV1owOC0xOTIiLCJXWjA4LTIwIiwiV1owOC0yMSIsIldaMDgtMjIiLCJXWjA4LTIzIiwiV1owOC0yMzEiLCJXWjA4LTIzMi0wMiIsIldaMDgtMjQiLCJXWjA4LTI0MS0wMiIsIldaMDgtMjQ0IiwiV1owOC0yNDUiLCJXWjA4LTI1IiwiV1owOC0yNiIsIldaMDgtMjciLCJXWjA4LTI4IiwiV1owOC0yOSIsIldaMDgtMzAiLCJXWjA4LTMxLTAyIiwiV1owOC0zMyIsIldaMDgtRCIsIldaMDgtMzUxLTAxIiwiV1owOC0zNTIiLCJXWjA4LUUiLCJXWjA4LTM2IiwiV1owOC0zNy0wMSIsIldaMDgtMzciLCJXWjA4LTM4LTAyIiwiV1owOC1GIiwiV1owOC00MS0wMSIsIldaMDgtNDMiLCJXWjA4LUciLCJXWjA4LTQ1IiwiV1owOC00NiIsIldaMDgtNDciLCJXWjA4LUgiLCJXWjA4LTQ5MS0wMSIsIldaMDgtNDkzLTAxIiwiV1owOC01MCIsIldaMDgtNTEiLCJXWjA4LTUyIiwiV1owOC01MyIsIldaMDgtSSIsIldaMDgtSiIsIldaMDgtSyIsIldaMDgtTCIsIldaMDgtTSIsIldaMDgtTiIsIldaMDgtTyIsIldaMDgtUCIsIldaMDgtUSIsIldaMDgtUi1UIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJJRCIsIkxBQkVMIl0sImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoidjQiLCJibG9ja0lkIjoiMC4wLjAifV0sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzEiLCJibG9ja0lkIjoiMC4wIn0seyJpZCI6ImMyLkVNUzAxMCIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImMyIiwiYmxvY2tJZCI6IjAuMSJ9LHsiaWQiOiJjMy5FTVMwMTEiLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjMyIsImJsb2NrSWQiOiIwLjIifSx7ImlkIjoiYzQuRU1TMDEyIiwidmFsdWVzSWRzIjpbIlFNVSJdLCJjaGlsZHJlbiI6W10sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzQiLCJibG9ja0lkIjoiMC4zIn0seyJpZCI6ImM1LkVNUzAxMyIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImM1IiwiYmxvY2tJZCI6IjAuNCJ9LHsiaWQiOiJjNi5FTVMwMTQiLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjNiIsImJsb2NrSWQiOiIwLjUifSx7ImlkIjoiYzcuRU1TMDE1IiwidmFsdWVzSWRzIjpbIlFNVSJdLCJjaGlsZHJlbiI6W10sInNob3dBc0ludGVybGluZSI6ZmFsc2UsImlzSGlkZGVuIjpmYWxzZSwiYmxvY2tDb2RlIjoiYzciLCJibG9ja0lkIjoiMC42In0seyJpZCI6ImM4LkVNUzAxNiIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImM4IiwiYmxvY2tJZCI6IjAuNyJ9LHsiaWQiOiJjOS5FTVMwMTciLCJ2YWx1ZXNJZHMiOlsiUU1VIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwiaXNIaWRkZW4iOmZhbHNlLCJibG9ja0NvZGUiOiJjOSIsImJsb2NrSWQiOiIwLjgifSx7ImlkIjoiYzEwLkVNUzAxOCIsInZhbHVlc0lkcyI6WyJRTVUiXSwiY2hpbGRyZW4iOltdLCJzaG93QXNJbnRlcmxpbmUiOmZhbHNlLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6ImMxMCIsImJsb2NrSWQiOiIwLjkifV0sInNob3dBc0ludGVybGluZSI6dHJ1ZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InYyIiwiYmxvY2tJZCI6IjAifV0sImNvbHVtbkhlYWRlciI6W3siaWQiOiJ2My5VTVdFTTIiLCJ2YWx1ZXNJZHMiOlsiRU1JUy1DTzIiLCJFTUlTLUNINCIsIkVNSVMtTjJPIiwiRU1JUy1OSDMiLCJFTUlTLVNPWCIsIkVNSVMtTk9YIiwiRU1JUy1OTVZPQyIsIkVNSVMtRlMxMCIsIkVNSVMtRlMyLTUiLCJFTUlTLUNPIl0sImNoaWxkcmVuIjpbXSwic2hvd0FzSW50ZXJsaW5lIjpmYWxzZSwic2hvd1ZhcmlhYmxlIjp0cnVlLCJzaG93VmFyaWFibGVWYWx1ZSI6WyJMQUJFTCJdLCJpc0hpZGRlbiI6ZmFsc2UsImJsb2NrQ29kZSI6InYzIiwiYmxvY2tJZCI6IjAifV0sImlzVHJhbnNwb3NlZCI6ZmFsc2V9)
* Data Type: CSV, XLSX

Unlike the other data sources, this source does not have a direct downloadable file link. Therefore, Selenium is used to subsitute manual work. This dataset contains information about the types of gases emitted and the sectors responsible in 2020.

### Datasource3: Air Emissions in 2021 
* Metadata URL: https://www.govdata.de/ckan/dataset/luftemisions-deutschland-jahre-luftemissionsartenwirtschaftszweige.rdf
* Data URL: https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0002_00.csv
* Data Type: CSV

This dataset contains information about the types of gases emitted and the sectors responsible in 2021.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Retrieve datasets and merge accordingly [#1][i1] 
2. Document the data [#2][i2]
3. Identify economic sectors with the highest gas emissions [#3][i3]
4. Visualize every gas type for selected economic sectors in a specific year [#4][i4]
5. Aggregate the amount of air emissions in each year [#5][i5]
6. Compare 2020 and 2021 with other years [#6][i6]
7. Visualize the proportion of each sector in a year [#7][i7]
8. Identify the sectors who contribute the most to air emissions [#8][i8]

[i1]: https://github.com/AyseAsude/FAU-MADE/issues/1
[i2]: https://github.com/AyseAsude/FAU-MADE/issues/2
[i3]: https://github.com/AyseAsude/FAU-MADE/issues/3
[i4]: https://github.com/AyseAsude/FAU-MADE/issues/4
[i5]: https://github.com/AyseAsude/FAU-MADE/issues/5
[i6]: https://github.com/AyseAsude/FAU-MADE/issues/6
[i7]: https://github.com/AyseAsude/FAU-MADE/issues/7
[i8]: https://github.com/AyseAsude/FAU-MADE/issues/8
