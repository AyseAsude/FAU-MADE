import pandas as pd
import numpy as np
import chardet
import requests


def main():
    data_source_1 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0001_00.csv"
    data_source_2 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0002_00.csv"
    data_source_3 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0003_00.csv"

 
    encoding_1 = get_encoding(data_source_1)
    # encoding_2 = get_encoding(data_source_2)
    # encoding_3 = get_encoding(data_source_3)

    
    data_till_2019 = pd.read_csv(data_source_1, delimiter=";", header=None, encoding=encoding_1, skiprows=6, skipfooter=3)
    # data_in_2021 = pd.read_csv(data_source_2, delimiter=";", header=None, encoding=encoding_2, skiprows=6, skipfooter=3)
    # data_in_2022 = pd.read_csv(data_source_3, delimiter=";", header=None, encoding=encoding_3, skiprows=6, skipfooter=3)

    transform_2019_data(data_till_2019)
    

    


def transform_2019_data(data_till_2019):
    # in the data_source_1, columns are years (1995, 1996, 1997, ..., 2019) rows are air emission types, eceonomic sectors, and their
    # corresponding values. For example column 1, row 1 till X correspond to carbondioxide, X+1 till Y correspond to methan, whereas column 3 corresponds to economic sectors. 
    # Other two datasets have air emission types as columns, rows as years, and economic sectors. In order to be consistent, data source 1 needs to be converted to the same form
    # as the other two datasets.

    # extract the years from the dataset, which are in the first row and have first 3 values empty
    years = data_till_2019.iloc[0].tolist()[3:]
    

    #data_till_2019 = data_till_2019.rename(columns={0: "air_emission_type", 2: "economic sector"})
    
    new_column_names = ["air_emission_type", "economic_sector"] + years
    # delete the second column, it holds no useful information
    data_till_2019 = data_till_2019.drop([1], axis="columns")



    data_till_2019.columns = new_column_names
    # removes the first row which incorrectly containes year information
    data_till_2019 = data_till_2019.iloc[1:]

    air_emission_types = data_till_2019.iloc[:,0].unique().tolist()
    print(air_emission_types)

    air_emissions_and_sectors_df = data_till_2019.iloc[:, :2]
    for year in years:
        temp_df = pd.concat([air_emissions_and_sectors_df, data_till_2019[year]], axis=1)  
        temp_df = pd.pivot(temp_df,index="economic_sector", columns="air_emission_type", values=year).reset_index()
        temp_df.insert(0, "year", year)
        filename = f"../data/Luftemissionen_{year}.csv"
        temp_df.to_csv(path_or_buf=filename, sep=";", index=False)
        


def get_encoding(url):
    response = requests.get(url)
    result = chardet.detect(response.content)
    encoding = result['encoding']
    return encoding

if __name__ == "__main__":
    main()