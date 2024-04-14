import pandas as pd


class DataTransform:
    """
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
        specify which symbols element.e., columns are
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

    """
    
    def __init__(self):
        """
        Initialiser.
        
        df: DataFrame
            The pandas dataframe containing
            the data.
        """
        pass

    def excess_symbol_removal(self, df, symbols):
        """
        When called, will remove any symbols which
        are not deemed necessary for our EDA goals.
        Must accept arguments which go on to
        specify which symbols element.e., columns are
        to be removed.
        """
        #symbols = str(input('separate by spaces which columns are to be dropped: ')).split()
        print('These are the symbols that will be dropped: ',symbols)
        df = df.drop(labels=symbols, axis=1, )
        remaining_symbols = []
        for element in df:
            remaining_symbols.append(element)
        print('These are the remaining symbols: ', remaining_symbols)
        return df
    
    def to_categorical(self, df, list_of_to_categorical):
        """
        When called, will convert column values
        to a categorical form.
        """
        for element in list_of_to_categorical:
            df[element] = df[element].astype("category")
        return df
    
    def to_boolean(self, df, list_of_to_boolean):
        """
        Goes from a numerical to a boolean pandas type
        """
        for element in list_of_to_boolean:
            df[element] = df[element].astype("bool")
        return df
    
    def to_float(self, df, list_of_to_float):
        """
        Goes from int to float
        """
        for element in list_of_to_float:
            df[element] = df[element].astype("float")
        return df
    
    def to_int(self, df, list_of_to_int):
        """
        Goes from float to int
        """
        for element in list_of_to_int:
            df[element] = df[element].astype("int")
        return df
    
    def convert_dates_to_proper_format(self, df, dates_to_convert):
        """
        Converts dates to the proper format
        """
        for element in dates_to_convert:
            df[element] = pd.to_datetime(df[element])
        return df

if __name__ == '__main__':
    pass