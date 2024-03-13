import psycopg2 as ps
import yaml
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect
from sqlalchemy import text

def function_to_load_credentials():
    with open("credentials.yaml", "r") as f:
        credentials = yaml.safe_load(f)
    return credentials
credentials = function_to_load_credentials() # to be passed to RDSDatabaseConnector

class RDSDatabaseConnector:
    def __init__(self, credentials = credentials):
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
    
    def initialise_engine(self):
        engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return engine

    def extract_data(self):
        print('string')
        engine = self.initialise_engine()
        en = engine.connect()
        loan_payments = pd.read_sql_table('loan_payments', en)
        df = pd.DataFrame(loan_payments)
        #print(df)
        return df
    
    def save_dataframe_as_csv(self):
        my_data_frame = self.extract_data()
        my_data_frame.to_csv('data.csv', index=False)

        

###
RDS = RDSDatabaseConnector()
e = RDS.initialise_engine()
print(e)
###

###
d = RDS.extract_data()
print(d)
###

###
f = RDS.save_dataframe_as_csv()
print(f)
###