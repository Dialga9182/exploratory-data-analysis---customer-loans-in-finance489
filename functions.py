import yaml
import pandas as pd

def function_to_load_credentials() -> dict:
    """Reads and returns credentials from YAML file.
        
    Parameters:
    -----------
    credentials: python object
        Contains the necessary credentials for use
        in authorising access to remote database information.
    """
    with open("credentials.yaml", "r") as f:
        credentials = yaml.safe_load(f)
    return credentials

def display_suggested_drops(dataframe: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """Print out the column names and the percentage of non-nulls in that column.
    This function prints out the column names
    and the percentage of non-nulls in that column.
    
    Parameters:
    -----------
    """
    acceptable_null_percentage = input('Acceptable Null percentage per column?: ')
    suggested_drops = []
    for element in dataframe: #displays: element, non_null count, non_null%.
        non_null_count = dataframe[element].count()
        total_count = dataframe.shape[0]
        percentage_non_null = (non_null_count / total_count) * 100
        if percentage_non_null < float(acceptable_null_percentage): # If <condition> Drop column.
            suggested_drops.append(element)
    print("Suggest dropping these columns: \n", suggested_drops) #suggests columns to be dropped
    return acceptable_null_percentage

def column_drop(dataframe: pd.core.frame.DataFrame, acceptable_null_percentage) -> pd.core.frame.DataFrame:
    dropped_columns = []
    for element in dataframe:
        non_null_count = dataframe[element].count()
        total_count = dataframe.shape[0]
        percentage_non_null = (non_null_count / total_count) * 100
        if percentage_non_null < float(acceptable_null_percentage): # If <condition> Drop column.
            dataframe.drop(element, axis=1, inplace=True)
            dropped_columns.append(element)
    print("Dropped columns: \n", dropped_columns)
    return dataframe, dropped_columns

if __name__ == '__main__':
    pass