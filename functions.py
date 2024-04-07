import yaml

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
