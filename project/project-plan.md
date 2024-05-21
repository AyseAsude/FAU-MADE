# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing Greenhouse Gas Emissions, Air Pollutants, and Economic Sector Interplay in Germany

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Which industries emit the most air pollutants and greenhouse gases?
2. How has industries' share of emissions evolved over the years?

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

### Datasource2: Air Emissions in 2021
* Metadata URL: https://www.govdata.de/ckan/dataset/luftemisions-deutschland-jahre-luftemissionsartenwirtschaftszweige.rdf
* Data URL: https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0002_00.csv
* Data Type: CSV

This dataset contains information about the types of gases emitted and the sectors responsible in 2021.

### Datasource3: Air Emissions in 2022
* Metadata URL: https://www.govdata.de/ckan/dataset/luftemisions-deutschland-jahre-entstehungsart-dermissions-luftemissionsarten-wirtschaftszwe.rdf
* Data URL: https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0003_00.csv
* Data Type: CSV

This dataset contains information about the types of gases emitted and the sectors responsible in 2022.
## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Retrieve datasets and merge accordingly [#1][i1] 
2. Document the data [#2][i2]

[i1]: https://github.com/AyseAsude/FAU-MADE/issues/1
[i2]: https://github.com/AyseAsude/FAU-MADE/issues/2