import yaml
from sqlalchemy import create_engine
import pandas as pd

def function_to_load_credentials():
    '''
    Creates a python object from a YAML file in the current working
    directory to be stored in a global variable.
    
    Parameters:
    -----------
    credentials: python object
    Contains the necessary credentials for use
    in authorising access to remote database information.
    '''
    with open("credentials.yaml", "r") as f:
        credentials = yaml.safe_load(f)
    return credentials
credentials = function_to_load_credentials()

class RDSDatabaseConnector:
    '''
    Facilitates the gathering and storing of tabular data
    for the purposes of later processing and exploratory
    data analysis.
    
    Parameters:
    -----------
    credentials: python object
        Contains the necessary credentials for use
        in authorising access to remote database information.
    
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
    def __init__(self, credentials = credentials):
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
        
        Parameters:
        -----------
        engine: Engine
            The engine required to extract data.
        encon: Connection
            A variable to enable a connection.
        loan_payments: DataFrame
            The loan_payments dataframe.
        df: DataFrame
            The dataframe in question.
        '''
        engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        encon = engine.connect()
        loan_payments = pd.read_sql_table('loan_payments', encon)
        df = pd.DataFrame(loan_payments)
        return df
    
    def save_dataframe_to_csv(self):
        '''
        Saves that dataframe to a csv file.
        
        Parameters:
        -----------
        my_data_frame: Dataframe
            The dataframe obtained from a pre-defined method.
        '''
        my_data_frame = self.initialise_engine_and_extract_data()
        my_data_frame.to_csv('data.csv', index=False)
    
    def load_dataframe_from_csv(self):
        '''
        Loads that dataframe from a csv file.
        
        Parameters:
        -----------
        df: Pandas DataFrame Object
            The dataframe in question.
        '''
        df = pd.read_csv('data.csv')
        column_names = []
        for i in df:
            column_names.append(i)
        print(column_names)
        return df

class DataTransform:
    '''
    This class holds methods which, when called, will
    transform the formats of certain columns in a table.
    PARAMETERS
    ATTRIBUTES
    METHODS
    '''
    def __init__(self, df = pd.read_csv('data.csv')):
        self.df = df
        pass
    def excess_symbol_removal(self):
        '''
        When called, will remove any symbols which
        are not deemed necessary for our EDA goals
        Must accept arguments which go on to
        specify which symbols i.e., columns are
        to be removed.
        '''
        symbols = str(input('separate by spaces which columns are to be dropped: ')).split()
        print('These are the symbols that will be dropped: ',symbols)
        self.df = self.df.drop(labels=symbols, axis=1, )
        remaining_symbols = []
        for i in self.df:
            remaining_symbols.append(i)
        print('These are the remaining symbols: ', remaining_symbols)
        return self.df
    def numerical_to_categorical(self):
        '''
        When called, will convert column values
        from a numerical form to a categorical form.
        Depending on the data involved, there could
        be many categories. For instance:
        1,2,3, to One, Two, Three.
        '''
                
        self.df['term'] = self.df['term'].astype("category")
        self.df['grade'] = self.df['grade'].astype("category") #made into category type!
        #TODO: Grade was not originally a numerical, so one might want to consider changing the method name
        #to something more like 'general_to_categorical' or something similar. Also change description too.
        self.df['sub_grade'] = self.df['sub_grade'].astype("category")
        self.df['home_ownership'] = self.df['home_ownership'].astype("category")
        self.df['verification_status'] = self.df['verification_status'].astype("category")
        self.df['loan_status'] = self.df['loan_status'].astype("category")
        self.df['payment_plan'] = self.df['payment_plan'].astype("category")
        self.df['purpose'] = self.df['purpose'].astype("category")
        self.df['delinq_2yrs'] = self.df['delinq_2yrs'].astype("category")
        self.df['application_type'] = self.df['application_type'].astype("category")
        #TODO: This ^^^^^ is tedious and it reuses code. Automate it.
        
        
        pass
    def numerical_to_boolean(self):
        '''
        Goes from a numerical to a boolean pandas type
        '''
        #TODO: Find a way to convert columns from numerical to boolean, i.e., int or float to bool
        # df['col'] = df['col'].astype('bool')
        #TODO: Find some columns where this might be useful.
        # 'policy_code' perhaps, although I will have to check if there
        # are other policy codes other than '1' as if there are others that aren't 1 or 0 then
        # it would likely be better as a category anyway
        
        #seeing as though there is only one policy code, i.e., '1'
        #there is no need to convert any of the columns to boolean
        #as this was the only column I thought might even need
        #converting to begin with...
        pass
    def categorical_to_boolean(self):
        # df['col'] = df['col'].astype('bool')
        pass
    def int_to_float(self):
        # df['col'] = df['col'].astype('float')
        pass
    def float_to_int(self):
        # df['col'] = df['col'].astype('int')
        pass
    def convert_dates_to_proper_format(self):
        #TODO: Figure out what the 'proper' format is.
        self.df['issue_date'] = pd.to_datetime(self.df['issue_date'])
        self.df['earliest_credit_line'] = pd.to_datetime(self.df['earliest_credit_line'])
        self.df['last_payment_date'] = pd.to_datetime(self.df['last_payment_date'])
        self.df['next_payment_date'] = pd.to_datetime(self.df['next_payment_date'])
        self.df['last_credit_pull_date'] = pd.to_datetime(self.df['last_credit_pull_date'])
        pass
    def method8():
        pass
    def method9():
        pass
    def add_more_methods_as_necessary():
        pass
    
class DataFrameInfo:
    '''DOCSTRING'''
    def __init__(self, df2):
        self.df2 = df2
        pass
    def method1_describe_all_columns_to_check_their_datatypes(self):
        print(self.df2.dtypes)
        pass
    def method2_extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(self):
        print(self.df2.describe()) # gives everything but the median.
        print(self.df2.median(numeric_only=True))
        pass
    def method3_count_distinct_values_in_categorical_columns(self):
        print(self.df2.nunique())
        pass
    def method4_print_out_the_shape_of_the_dataframe(self):
        print(self.df2.shape)
        pass
    def method5_generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(self):
        print(self.df2.isnull().count())#.count(),
        #TODO: Must still generate percentage count of nulls in each column
        pass
    def method6_anyothermethodsyoufinduseful():
        pass
    '''
    Describe all columns in the DataFrame to check their data types
Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
Count distinct values in categorical columns
Print out the shape of the DataFrame
Generate a count/percentage count of NULL values in each column
Any other methods you may find useful'''
    pass

def amount_of_nulls_and_column_drop():
    #determine the amount of NULLs in each column. 
    #Determine which columns should be dropped and drop them.
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
    RDS = RDSDatabaseConnector()
    a = RDS.initialise_engine_and_extract_data()
    b = RDS.save_dataframe_to_csv()
    c = RDS.load_dataframe_from_csv()
    DT = DataTransform()
    d = DT
    e = DT
    f = DT