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
    def __init__(self, DT = DataTransform):
        '''
        desc
        
        Parameters:
        -----------
        df2: DataFrame
            Contains the dataframe previously
            worked on
        '''
        self.df2 = DT.convert_dates_to_proper_format()
        pass
    
    def describe_all_columns_to_check_their_datatypes(self):
        '''
        Describe all columns in the DataFrame to check their data types
        '''
        print(self.df2.dtypes)
        pass
    
    def extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(self):
        '''
        Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
        '''
        print(self.df2.describe()) # gives everything but the median.
        print(self.df2.median(numeric_only=True))
        pass
    
    def count_distinct_values_in_categorical_columns(self):
        '''
        Count distinct values in categorical columns
        '''
        print(self.df2.nunique())
        pass
    
    def print_out_the_shape_of_the_dataframe(self):
        '''
        Print out the shape of the DataFrame
        '''
        print(self.df2.shape)
    
    def generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(self):
        '''
        Generate a count/percentage count of NULL values in each column
        '''
        print('Number of Non-nulls in the column values for id:')
        print(self.df2['id'].isnull().count())#.count(),
        #TODO: Must still generate percentage count of nulls in each column
        #print('')
        return self.df2
    pass


def amount_of_nulls_and_column_drop(DFI = DataFrameInfo):
    '''
    desc
    
    Parameters:
    -----------
    '''
    #print('COLUMN NAMES AND NO. OF NON-NULL VALUES IN COLUMN')
    df = DFI.generate_a_count_slash_percentage_count_of_NULL_values_in_each_column()
    for i in df:
        print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
        #determine a percentage of nulls that is acceptable
        #if non-nulls < 80% of total dataset, drop column
        
 
    #Determine which columns should be dropped and drop them.
    #if null nums > certain number, drop cols with that number of nulls.
    pass


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



#TODO: Find a way to use fewer self variables
# Assign a variable before calling any method inside of a class
# Maybe use global variables, although this was less clear
# Read that notebook from before!!!

# I feel like my classes are not very linked...
# I feel like I cant pass the dataframes between the classes very easily
# How do I implement a way to take my dataframe out of the classes and update it on its own using the classes
# I feel there is something fundamental that has gone wrong here but I cannot tell what it is...



#Refactor code such that we do not pass the dataframe through the functions/classes
#within the db_utils file but instead it is parsed as an external parameter
#taken from the analysis_and_querying file!!!

#TODO: Create a whole new repository focused on the imagined
#refactoring of my code here but based on the principle that
#all classes/functions will have to accept an external
#parameter df, which is to be the pandas dataframe containing
#all the relevant data to be manipulated and analysed.

#TODO: Make a decision about the yaml file...
#Problem, last time I tried to experiment with
#another repository for this project, the
#interaction between the code and the yaml
#file didn't seem to work.
#To get around this I hard coded the relevant
#content contained within the yaml file directly
#into the relevant area of the code.
#I don't see a technical reason why not to do this
#again, but it may well make it confusing for
#me to deal with later on...
#Decision made, hard coding now.