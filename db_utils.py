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
        self.engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        return table_names

    def extract_data(self):
        print('string')
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM loan_payments LIMIT 10"))
            for row in result:
                print(row)

###
RDS = RDSDatabaseConnector()
e = RDS.initialise_engine()
print(e)
###

###
d = RDS.extract_data()
print(d)
###
