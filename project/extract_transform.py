"""
Data source: Statistisches Bundesamt (Destatis), Genesis-Online, Date of retrieval: June 4, 2024;
Data licence by-2-0: https://www.govdata.de/dl-de/by-2-0
"""


import pandas as pd
import chardet
import requests
import time


def main():

    data_source_1 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0001_00.csv"
    data_source_2 = f"../data/Luftemissionen_2020_not_transformed.csv"
    data_source_3 = "https://www-genesis.destatis.de/genesis/downloads/00/tables/85111-0002_00.csv"

    encoding_1 = check_and_get_encoding(data_source_1)
    encoding_3 = check_and_get_encoding(data_source_3)
 
    # Document contains some metadata in the first rows and in the footer, so they are discarded 
    data_till_2019 = load(data_source_1, encoding_1)
    print(data_till_2019.iloc[:6, :10])
    data_in_2020 = load(data_source_2)
    data_in_2021 = load(data_source_3, encoding_3)
        
    transform_2019_data(data_till_2019)
    
    data_in_2020 = transform_2020(data_in_2020)
    transform_data(data_in_2020)
    
    transform_data(data_in_2021)

def load(data_source, encoding="utf-8"):
    return pd.read_csv(data_source, delimiter=";", header=None, encoding=encoding, skiprows=6, skipfooter=3, engine='python')

def transform_2020(df):

    # first 5 values are also NaN in 2021 data, so they are skipped
    header = df.iloc[0, 5:]

    # identifies NaN columns
    nan_idx = header.isna()
    nan_idx = nan_idx[nan_idx == True].index
    
    # In order to be in the same format as 2021, set constant values for the first two columns and drop the NaN columns
    df.iloc[:, 0] = 2020
    df = df.drop(columns=nan_idx)
    df.iloc[:, 1].fillna("Luftemissionen", inplace=True)

    return df


def transform_data(df):

    # drop columns 2, 3, 5; they do not hold useful information
    df = df.drop([1, 2, 4], axis="columns")

    # year and economic sector column names do not exist in the original dataset, so add them to the dataframe
    gas_types = df.iloc[0].tolist()[2:]
    new_col_names = ["year", "economic_sector"] + gas_types
    df.columns = new_col_names

    # remove the first row which incorrectly contains information
    df = df.iloc[1:]

    # year is in float type, convert it to integer
    df["year"] = df["year"].astype(int)
    year_info = df.iloc[0,0]

    save_as_csv(df, year_info)
        


def transform_2019_data(data_till_2019):
    """In the data_source_1, columns are years (1995, 1996, 1997, ..., 2019) rows are air emission types, 
    eceonomic sectors, and their corresponding values. For example column 1, row 1 till X correspond to 
    carbondioxide, X+1 till Y correspond to methan, whereas column 3 corresponds to economic sectors.
    The other dataset have air emission types as columns, rows as years, and economic sectors. In order 
    to be consistent, data source 1 needs to be converted to the same form
    as the other two datasets.
    """

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

    filenames = []
    # creates a csv file for each year
    for year in years:
        # extract the current year and append it
        temp_df = pd.concat([air_emissions_and_sectors_df, data_till_2019[year]], axis=1)  
        
        # converts gas types as columns instead of repeating it in multiple rows
        temp_df = pd.pivot_table(temp_df,index="economic_sector", columns="air_emission_type", values=year, sort=False, aggfunc="first").reset_index()

        # added year information as a column
        temp_df.insert(0, "year", year)
        save_loc = save_as_csv(temp_df, year)
        filenames.append(save_loc)
    return filenames


def check_and_get_encoding(url, max_attempts=3, delay=1):
    """
    Tries to fetch the encoding of a web page from a given URL.
    
    Args:
        url (str): The URL of the web page.
        max_attempts (int, optional): Maximum number of attempts to make the request. Default is 3.
        delay (int, optional): Time to wait (in seconds) between each attempt. Default is 1 second.
    
    Returns:
        str or None: The encoding of the web page if successful, None otherwise.
    """
    attempt = 0
    while attempt < max_attempts:
        try:
            response = requests.get(url)
            if response.ok:
                result = chardet.detect(response.content)
                encoding = result['encoding']
                return encoding
            else:
                print(f"Failed to request URL: {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to request URL: {url}. Error: {str(e)}")

        time.sleep(delay)
        attempt += 1

    print(f"Failed to request URL: {url} after {max_attempts} attempts.")
    return None


def save_as_csv(df, year):
    """
    Saves a DataFrame to a CSV file.

    Args:
        df (DataFrame): The DataFrame to be saved.
        year (int): The year associated with the data being saved.

    Returns:
        None
    """
    filename = f"../data/Luftemissionen_{year}.csv"
    df.to_csv(path_or_buf=filename, sep=";", index=False)
    return filename

if __name__ == "__main__":
    main()