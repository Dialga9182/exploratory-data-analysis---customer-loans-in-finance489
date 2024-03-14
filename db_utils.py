import yaml
from sqlalchemy import create_engine
import pandas as pd

def function_to_load_credentials():
    with open("credentials.yaml", "r") as f:
        credentials = yaml.safe_load(f)
    return credentials
credentials = function_to_load_credentials()

class RDSDatabaseConnector:
    def __init__(self, credentials = credentials):
        self.host = credentials['RDS_HOST']
        self.password = credentials['RDS_PASSWORD']
        self.user = credentials['RDS_USER']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
    
    def initialise_engine_and_extract_data(self):
        engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        encon = engine.connect()
        loan_payments = pd.read_sql_table('loan_payments', encon)
        df = pd.DataFrame(loan_payments)
        return df
    
    def save_dataframe_to_csv(self):
        my_data_frame = self.initialise_engine_and_extract_data()
        my_data_frame.to_csv('data.csv', index=False)
    
    def load_dataframe_from_csv(self):
        df = pd.read_csv('data.csv')
        print(df.shape)

if __name__=='__main__':
    RDS = RDSDatabaseConnector()
    a = RDS.initialise_engine_and_extract_data()
    b = RDS.save_dataframe_to_csv()
    c = RDS.load_dataframe_from_csv()
    