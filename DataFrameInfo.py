class DataFrameInfo:
    """Perform EDA transformations on the data.
    Performs EDA transformations on the data
    
    Parameters:
    -----------
    None
    
    Attributes:
    -----------
    None
    
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
    """
    
    def __init__(self):
        """Initialise.
        An instance method for DataFrameInfo
        
        Parameters:
        -----------
        None
        """
        pass
    
    def describe_all_columns_to_check_their_datatypes(self, df):
        """Describe all columns in the DataFrame to check their data types.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(df.dtypes)
        return df
    
    def extract_statistical_values_median_stddev_mean_from_cols_and_dataframe(self, df):
        """Extract statistical values: median, standard deviation and mean from the columns and the DataFrame.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(df.describe()) # gives everything but the median.
        print('Medians for each column: \n')
        print(df.median(numeric_only=True))
        return df
    
    def count_distinct_values_in_categorical_columns(self, df):
        """Count distinct values in categorical columns.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(df.nunique())
        return df
    
    def print_out_the_shape_of_the_dataframe(self, df):
        """Print out the shape of the DataFrame.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(df.shape)
        return df
    
    def generate_a_count_slash_percentage_count_of_NULL_values_in_each_column(self, df):
        """Generate a count/percentage count of NULL values in each column.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """        """"""
        for element in df:
            non_null_count = df[element].count()
            total_count = df.shape[0]
            percentage_non_null = (non_null_count / total_count) * 100
            print(element, ': Non-nulls:', non_null_count, 'Non-Null Percentage:', percentage_non_null, '%')
            #determine a percentage of nulls that is acceptable
            #if non-nulls < 80% of total dataset, drop column
            #if (((df[element].isnull().count())/(df.shape[0]))*100) < 80:
                #df.drop(element, index = 1)
        return df
    
    """
    should probably have sorted out a few lists regarding numeric, non-numeric,
    categorical, datetimes etc for use as a copy-paste tool.
    
    yeah thats a good idea, you can put that into your DataInfo
    class or whatever its called


    """
    
if __name__ == '__main__':
    pass