from sqlalchemy import create_engine
import pandas as pd

RDS_HOST= 'eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com'
RDS_PASSWORD= 'EDAloananalyst'
RDS_USER= 'loansanalyst'
RDS_DATABASE= 'payments'
RDS_PORT= 5432


class RDSDatabaseConnector:
    
    def __init__(self, RDS_HOST = RDS_HOST):
        self.host = RDS_HOST
        self.password = RDS_PASSWORD
        self.user = RDS_USER
        self.database = RDS_DATABASE
        self.port = RDS_PORT
    
    def initialise_engine_and_extract_data(self):
        engine = create_engine(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}")
        encon = engine.connect()
        loan_payments = pd.read_sql_table('loan_payments', encon)
        df = pd.DataFrame(loan_payments)
        return df
    
    def save_dataframe_to_csv(self):
        df = self.initialise_engine_and_extract_data()
        df.to_csv('data.csv', index=False)
        pass
    
    def load_dataframe_from_csv(self):
        df = pd.read_csv('data.csv')
        return df

class DataTransform:
    def __init__(self):
        pass
    
    def excess_symbol_removal(self, df, symbols):
        print('These are the symbols that will be dropped: ',symbols)
        df = df.drop(labels=symbols, axis=1, )
        remaining_symbols = []
        for i in df:
            remaining_symbols.append(i)
        print('These are the remaining symbols: ', remaining_symbols)
        return df
    
    def to_categorical(self, df, list_of_to_categorical):
        for i in list_of_to_categorical:
            df[i] = df[i].astype("category")
        return df
    
    def to_boolean(self, df, list_of_to_boolean):
        for i in list_of_to_boolean:
            df[i] = df[i].astype("bool")
        return df
    
    def to_float(self, df, list_of_to_float):
        for i in list_of_to_float:
            df[i] = df[i].astype("float")
        return df
    
    def to_int(self, df, list_of_to_int):
        for i in list_of_to_int:
            df[i] = df[i].astype("int")
        return df
    
    def convert_dates_to_proper_format(self, df, dates_to_convert):
        for i in dates_to_convert:
            df[i] = pd.to_datetime(df[i])
        return df

class DataFrameInfo:
    
    def __init__(self):
        pass
    
    def describe_all_columns_to_check_their_datatypes(self, df):
        print(df.dtypes)
        return df
    
    def extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(self, df):
        print(df.describe())
        print('Medians for each column: \n')
        print(df.median(numeric_only = True))
        return df
    
    def count_distinct_values_in_categorical_columns(self, df):
        print(df.nunique())
        return df
    
    def print_out_the_shape_of_the_dataframe(self, df):
        print(df.shape)
        return df
    
    def generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(self, df):
        for i in df:
            print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
            #determine a percentage of nulls that is acceptable
            #if non-nulls < 80% of total dataset, drop column
            #if (((df[i].isnull().count())/(df.shape[0]))*100) < 80:
                #df.drop(i, index = 1)
        return df

def amount_of_nulls_and_column_drop(df):
    for i in df.columns:
        print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
        #determine a percentage of nulls that is acceptable
        #if non-nulls < 80% of total dataset, drop column
        if (((df[i].isnull().count())/(df.shape[0]))*100) < 101:
            #print('NOW DROPPING COLUMNS')
            df.drop(columns = i)
    return df


if __name__ == '__main__':
    RDS = RDSDatabaseConnector()
    #b = RDS.initialise_engine_and_extract_data()
    #c = RDS.save_dataframe_to_csv()
    df = RDS.load_dataframe_from_csv()
    
    DT = DataTransform()
    #symbols = str(input('separate by spaces which columns are to be dropped: ')).split()
    #df = DT.excess_symbol_removal(df, symbols)
    
    list_of_to_categorical = ['term','grade','sub_grade','home_ownership','verification_status','loan_status','payment_plan','purpose','delinq_2yrs','application_type']
    #df = DT.to_categorical(df, list_of_to_categorical)
    
    list_of_to_boolean = []
    #df = DT.to_boolean(df, list_of_to_boolean)
    
    list_of_to_float = []
    #df = DT.to_float(df, list_of_to_float)
    
    list_of_to_int = []
    #df = DT.to_int(df, list_of_to_int)
    
    dates_to_convert = ['issue_date','earliest_credit_line','last_payment_date','next_payment_date','last_credit_pull_date']
    #df = DT.convert_dates_to_proper_format(df, dates_to_convert)
    
    DFI = DataFrameInfo()
    #df = DFI.describe_all_columns_to_check_their_datatypes(df)
    
    #df = DFI.extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(df)
    
    #df = DFI.count_distinct_values_in_categorical_columns(df)
    
    #df = DFI.print_out_the_shape_of_the_dataframe(df)
    
    #df = DFI.generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(df)
    
    #df = amount_of_nulls_and_column_drop(df)
    
print('HERE TO DROP COLUMNS BEGIN')
for i in df.columns:
        print(i, ':', 'Non-nulls: ', (df[i].isnull().count()), 'Non-Null= ', (((df[i].isnull().count())/(df.shape[0]))*100),'%')
        #determine a percentage of nulls that is acceptable
        #if non-nulls < 80% of total dataset, drop column
        if (((df[i].isnull().count())/(df.shape[0]))*100) < 101:
            print('NOW DROPPING COLUMNS')
            df.drop(columns = i, inplace=False)
print(df)
print('HERE TO DROP COLUMNS END')