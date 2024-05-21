import pandas as pd
import numpy as np
import chardet
import requests


def main():
    data_source_1 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0001_00.csv"
    data_source_2 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0002_00.csv"

 
    encoding_1 = get_encoding(data_source_1)
    encoding_2 = get_encoding(data_source_2)

    
    data_till_2019 = pd.read_csv(data_source_1, delimiter=";", header=None, encoding=encoding_1, skiprows=6, skipfooter=3)
    data_in_2021 = pd.read_csv(data_source_2, delimiter=";", header=None, encoding=encoding_2, skiprows=6, skipfooter=3)

    transform_2019_data(data_till_2019)
    transform_data(data_in_2021)
    
def transform_data(df):

    # drop columns 2, 3, 5; they hold unuseful information
    df = df.drop([1, 2, 4], axis="columns")
    gas_types = df.iloc[0].tolist()[2:]
    new_col_names = ["year", "economic_sector"] + gas_types
    df.columns = new_col_names

    # remove the first row which incorrectly contains information
    df = df.iloc[1:]
    # year is in float type, convert it to integer
    df["year"] = df["year"].astype(int)
    year_info = df.iloc[0,0]
    filename = f"../data/Luftemissionen_{year_info}.csv"
    df.to_csv(path_or_buf=filename, sep=";", index=False)
        


def transform_2019_data(data_till_2019):
    # in the data_source_1, columns are years (1995, 1996, 1997, ..., 2019) rows are air emission types, eceonomic sectors, and their
    # corresponding values. For example column 1, row 1 till X correspond to carbondioxide, X+1 till Y correspond to methan, whereas column 3 corresponds to economic sectors. 
    # Other two datasets have air emission types as columns, rows as years, and economic sectors. In order to be consistent, data source 1 needs to be converted to the same form
    # as the other two datasets.

    # extract the years from the dataset, which are in the first row and have first 3 values empty
    years = data_till_2019.iloc[0].tolist()[3:]
    
    
    new_column_names = ["air_emission_type", "economic_sector"] + years
    # delete the second column, it holds no useful information
    data_till_2019 = data_till_2019.drop([1], axis="columns")



    data_till_2019.columns = new_column_names
    # remove the first row which incorrectly contains year information
    data_till_2019 = data_till_2019.iloc[1:]

    # used to transform common gas types' and ecenomic sectors'name
    air_emissions_and_sectors_df = data_till_2019.iloc[:, :2]

    # creates a csv file for each year
    for year in years:

        # extract the current year and append it
        temp_df = pd.concat([air_emissions_and_sectors_df, data_till_2019[year]], axis=1)  
        # converts gas types as columns instead of repeating it in multiple rows
        temp_df = pd.pivot_table(temp_df,index="economic_sector", columns="air_emission_type", values=year, sort=False, aggfunc="first").reset_index()
        print(temp_df)

        # added year information as a column
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