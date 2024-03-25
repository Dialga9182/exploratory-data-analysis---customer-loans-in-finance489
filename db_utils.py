import yaml
from sqlalchemy import create_engine
import pandas as pd

def function_to_load_credentials():
    '''
    Creates a python object from a YAML file.
    
    Parameters:
    -----------
    credentials: python object
        Contains the necessary credentials for use
        in authorising access to remote database information.
    '''
    with open("credentials.yaml", "r") as f:
        credentials = yaml.safe_load(f)
    return credentials


class RDSDatabaseConnector:
    '''
    Facilitates the gathering and storing of tabular data
    for the purposes of later processing and exploratory
    data analysis.
    
    Parameters:
    -----------
    credentials: python object
        Contains the necessary credentials for use in
        authorising access to remote database information.
    
    Attributes:
    -----------
    host: str
        The link to the connection required to access
        the data.
    password: str
        The password.
    user: str
        The user.
    database: str
        The name of the database.
    port: int
        The port.
    
    Methods:
    --------
    initialise_engine_and_extract_data(self)
        Initialises the engine, extracts the
        data from the location where it is stored,
        and then saves that as a pandas dataframe.
    save_dataframe_to_csv(self)
        Saves that pandas dataframe to a csv file.
    load_dataframe_from_csv(self)
        Loads that dataframe from a csv file.
    '''
    def __init__(self, credentials = function_to_load_credentials()):
        '''
        Initialiser.
        
        Parameters:
        -----------
        credentials: python object
            Contains the necessary credentials for use in
            authorising access to remote database information.
        '''
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        
    
    def initialise_engine_and_extract_data(self):
        '''
        Initialises the engine, extracts the
        data from the location where it is stored,
        and then saves that as a pandas dataframe.
        '''
        engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        encon = engine.connect()
        loan_payments = pd.read_sql_table('loan_payments', encon)
        df = pd.DataFrame(loan_payments)
        return df
    
    def save_dataframe_to_csv(self):
        '''
        Saves that dataframe to a csv file.
        '''
        df = self.initialise_engine_and_extract_data()
        df.to_csv('data.csv', index=False)
    
    def load_dataframe_from_csv(self):
        '''
        Loads that dataframe from a csv file.
        '''
        df = pd.read_csv('data.csv')
        '''#column_names = []
        #for i in df:
        #    column_names.append(i)
        #print(column_names)'''
        return df


class DataTransform:
    '''
    This class holds methods which, when called, will
    transform the formats of certain columns in a table.
    
    Parameters:
    -----------
    df: DataFrame
        The pandas dataframe containing
        the data.
    
    Attributes:
    -----------
    df: DataFrame
        The pandas dataframe containing
        the data.
    
    Methods:
    --------
    excess_symbol_removal()
        When called, will remove any symbols which
        are not deemed necessary for our EDA goals.
        Must accept arguments which go on to
        specify which symbols i.e., columns are
        to be removed.
    to_categorical()
        When called, will convert column values
        to a categorical form.
    numerical_to_boolean()
        Goes from a numerical to a boolean pandas type
    categorical_to_boolean()
        Goes from categorical to boolean
    int_to_float()
        Goes from int to float
    float_to_int()
        Goes from float to int
    convert_dates_to_proper_format()
        Converts dates to the proper format

    '''
    def __init__(self): #TODO:make it a variable and use less self.variables
        '''
        Initialiser.
        
        df: DataFrame
            The pandas dataframe containing
            the data.
        '''
        pass

    def excess_symbol_removal(self, df, symbols):
        '''
        When called, will remove any symbols which
        are not deemed necessary for our EDA goals.
        Must accept arguments which go on to
        specify which symbols i.e., columns are
        to be removed.
        '''
        #symbols = str(input('separate by spaces which columns are to be dropped: ')).split()
        print('These are the symbols that will be dropped: ',symbols)
        df = df.drop(labels=symbols, axis=1, )
        remaining_symbols = []
        for i in df:
            remaining_symbols.append(i)
        print('These are the remaining symbols: ', remaining_symbols)
        return df
    
    def to_categorical(self, df, list_of_to_categorical):
        '''
        When called, will convert column values
        to a categorical form.
        '''
        for i in list_of_to_categorical:
            df[i] = df[i].astype("category")
        return df
    
    def to_boolean(self, df, list_of_to_boolean):
        '''
        Goes from a numerical to a boolean pandas type
        '''
        for i in list_of_to_boolean:
            df[i] = df[i].astype("bool")
        return df
    
    def to_float(self, df, list_of_to_float):
        '''
        Goes from int to float
        '''
        for i in list_of_to_float:
            df[i] = df[i].astype("float")
        return df
    
    def to_int(self, df, list_of_to_int):
        '''
        Goes from float to int
        '''
        for i in list_of_to_int:
            df[i] = df[i].astype("int")
        return df
    
    def convert_dates_to_proper_format(self, df, dates_to_convert):
        '''
        Converts dates to the proper format
        '''
        for i in dates_to_convert:
            df[i] = pd.to_datetime(df[i])
        return df

    
class DataFrameInfo:
    '''
    Performs EDA transformations on the data
    
    Parameters:
    -----------
    df2: DataFrame
        Contains the dataframe previously
        worked on
    
    Attributes:
    -----------
    df2: DataFrame
        Contains the dataframe previously
        worked on
    
    Methods:
    --------
    describe_all_columns_to_check_their_datatypes()
        Describe all columns in the DataFrame to check their data types
    extract_statistical_values_median_stddev_mean_from_cols_and_dataframe()
        Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
    count_distinct_values_in_categorical_columns()
        Count distinct values in categorical columns
    print_out_the_shape_of_the_dataframe()
        Print out the shape of the DataFrame
    generate_a_count_slash_percentage_count_of_NULL_values_in_each_column()
        Generate a count/percentage count of NULL values in each column
    '''
    def __init__(self):
        '''
        desc
        
        Parameters:
        -----------
        df2: DataFrame
            Contains the dataframe previously
            worked on
        '''
        pass
    
    def describe_all_columns_to_check_their_datatypes(self, df):
        '''
        Describe all columns in the DataFrame to check their data types
        '''
        print(df.dtypes)
        return df
    
    def extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(self, df):
        '''
        Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
        '''
        print(df.describe()) # gives everything but the median.
        print('Medians for each column: \n')
        print(df.median(numeric_only=True))
        return df
    
    def count_distinct_values_in_categorical_columns(self, df):
        '''
        Count distinct values in categorical columns
        '''
        print(df.nunique())
        return df
    
    def print_out_the_shape_of_the_dataframe(self, df):
        '''
        Print out the shape of the DataFrame
        '''
        print(df.shape)
        return df
    
    def generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(self, df):
        '''
        Generate a count/percentage count of NULL values in each column
        '''
        for i in df:
            print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
            #determine a percentage of nulls that is acceptable
            #if non-nulls < 80% of total dataset, drop column
            #if (((df[i].isnull().count())/(df.shape[0]))*100) < 80:
                #df.drop(i, index = 1)
        return df


def amount_of_nulls_and_column_drop(df):
    '''
    desc
    
    Parameters:
    -----------
    '''
    for i in df:
        print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
        #determine a percentage of nulls that is acceptable
        #if non-nulls < 80% of total dataset, drop column
        if (((df[i].isnull().count())/(df.shape[0]))*100) < 101:
            df.drop(i, index = 1)
    return df


class DataFrameTransform:
    #create a method which can impute your DataFrame columns. 
    #Decide whether the column should be imputed with the median or the mean and 
    #impute the NULL values.
    pass

#Run your NULL checking method/function again to check that all NULLs have been removed.

class Plotter:
    #Generate a plot by creating a method in your Plotter class to visualise the removal of NULL values.
    pass


if __name__ == '__main__':
    pass
