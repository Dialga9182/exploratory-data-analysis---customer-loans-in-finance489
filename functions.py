import yaml
import pandas as pd

def function_to_load_credentials():
    """Reads and returns credentials from YAML file.
        
    Parameters:
    -----------
    credentials: python object
        Contains the necessary credentials for use
        in authorising access to remote database information.
    """
    with open("credentials.yaml", "r") as f:
        credentials: dict = yaml.safe_load(f)
    return credentials

def amount_of_nulls_and_column_drop(df: pd.core.frame.DataFrame):
    """Print out the column names and the percentage of non-nulls in that column.
    This function prints out the column names
    and the percentage of non-nulls in that column.
    
    Parameters:
    -----------
    """
    for element in df:
        non_null_count: pd.Series = df[element].count()
        total_count: pd.Series = df.shape[0]
        percentage_non_null: float = (non_null_count / total_count) * 100
        print(element, ': Non-nulls:', non_null_count, 'Non-Null Percentage:', percentage_non_null, '%')
        if percentage_non_null < 80: # If non-nulls < 80% of total dataset, drop column
            print(f"Dropping column '{element}' with non-null percentage {percentage_non_null:.2f}%")
            df.drop(element, axis=1, inplace=True)
    return df

if __name__ == '__main__':
    print(type(function_to_load_credentials()))
    pass