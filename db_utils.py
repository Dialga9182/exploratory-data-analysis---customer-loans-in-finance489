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
        Saves that dataframe to a csv file.
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
        print(df.shape)

if __name__=='__main__':
    RDS = RDSDatabaseConnector()
    a = RDS.initialise_engine_and_extract_data()
    b = RDS.save_dataframe_to_csv()
    c = RDS.load_dataframe_from_csv()
    