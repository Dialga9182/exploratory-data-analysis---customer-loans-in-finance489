import numpy as np


class DataFrameTransform:
    """
    This class imputes data where necessary
    and removes rows where necessary. 
    """
    
    def __init__(self):
        """DOCSTRING"""
        pass
    
    def impute(self, df):
        """
        This method imputes data where necessary
        and removes rows where necessary. 
        
        """
        df['funded_amount'] = df['funded_amount'].fillna(df['funded_amount'].mean())
        df['int_rate'] = df['int_rate'].fillna(df['int_rate'].mean())
        df['term'] = df['term'].fillna(df['term'].mode()[0])
        df['employment_length'] = df['employment_length'].fillna(df['employment_length'].mode()[0])
        
        df = df.dropna(subset=['last_payment_date'], inplace=False)
        #df = df.dropna(subset=['last_payment_date'], inplace=False)
        return df
    #Z-Score Method - VIDEO VERSION
    # trimming - delete the outlier data - from video
    def z_score_trim_vidver(self, df, columns):
        for element in df[(columns)]:
            upper_limit = df[element].mean() + 3*df[element].std()
            lower_limit = df[element].mean() - 3*df[element].std()
            df_z_score_vid_trim = df.loc[(df[element]<upper_limit) & (df[element]>lower_limit)]
        print(len(df)-len(df_z_score_vid_trim), 'outliers removed using zscore with vid trimming method')
        #plot_boxplots(df_z_score_vid_trim, columns)
        return df_z_score_vid_trim

    def z_score_cap_vidver(self, df, columns):
        df_z_score_vid_capping = df.copy()
        for element in df[(columns)]:
            upper_limit = df[element].mean() + 3*df[element].std()
            lower_limit = df[element].mean() - 3*df[element].std()
            
            #the before
            df_z_score_vid_capping.loc[df_z_score_vid_capping[element]>upper_limit, element] = upper_limit
            df_z_score_vid_capping.loc[df_z_score_vid_capping[element]<lower_limit, element] = lower_limit
        print(len(df)-len(df_z_score_vid_capping), 'outliers removed using zscore with vid capping method')
        #plot_boxplots(df_z_score_vid_capping, columns)
        return df_z_score_vid_capping

    #actually, len-len should be zero as they are now within the limits?
    # number of at limit items should increase but I dont know how to express that

    #Z-Score Method - NOTEBOOK VERSION
    def create_z_score_df(self, df, columns):
        df_with_zscore = df.copy() # new dataframe is a copy of old dataframe
        for element in df_with_zscore[(columns)]:
            #print(element)
            #print(np.mean(df_with_zscore[element]))
            mean_of_col = np.mean(df_with_zscore[element])
            std_of_col = np.std(df_with_zscore[element])
            z_scores = ((df_with_zscore[element] - mean_of_col) / std_of_col)
        df_with_zscore['z_scores'] = z_scores
        return df_with_zscore

    def trim_by_z_score(self, df, columns):
        df_with_zscore = self.create_z_score_df(df, columns)
        df_trimmed_by_z_score = df_with_zscore.loc[(df_with_zscore['z_scores']> -3) & (df_with_zscore['z_scores']<3)]
        print('Number of outliers trimmed: ', (len(df_with_zscore)-len(df_trimmed_by_z_score)))
        return df_trimmed_by_z_score

    def cap_by_z_score(self, df, columns):
        df_with_zscore = self.create_z_score_df(df, columns)
        def replace_by_z_score(dataframe, df_column, threshold=3): #caps a df
            mean = dataframe[df_column].mean()
            std = dataframe[df_column].std()
            # getting the outliers rows
            outliers = dataframe.loc[((dataframe[df_column] - mean) / std).abs() > threshold, df_column]
            # replacing the outlier rows with the mean of the column
            dataframe.loc[outliers.index, df_column] = mean
            return dataframe
        df_capped_by_z_score = df_with_zscore.copy()
        #print('Before Capping:\n', df_capped_by_z_score[(columns)].skew())
        #plot_boxplots(df_capped_by_z_score, columns)
        for element in df_capped_by_z_score[(columns)]:
            replace_by_z_score(df_capped_by_z_score, element)
        return df_capped_by_z_score
        #print('After Capping:\n', (df_capped_by_z_score[(columns)].skew()))
        #plot_boxplots(df_capped_by_z_score, columns)
        #print('Number of Capped outliers:', (len(df)-len(df_capped_by_z_score)))

    # IQR Method - from video, same as from notebook
    def get_upper_limit(self, df, columns):
        for element in df[(columns)]:
            q1 = df[element].quantile(0.25)
            q3 = df[element].quantile(0.75)
        IQR = q3-q1
        upper_limit = q3 + (1.5 * IQR)
        return upper_limit
    
    def get_lower_limit(self, df, columns):
        for element in df[(columns)]:
            q1 = df[element].quantile(0.25)
            q3 = df[element].quantile(0.75)
        IQR = q3-q1
        lower_limit = q1 - (1.5 * IQR)
        return lower_limit

    def trim_by_iqr_limits(self, df, columns):
        df_untrimmed_by_iqr = df.copy()
        for element in df_untrimmed_by_iqr[(columns)]:
            df_trimmed_by_iqr = df_untrimmed_by_iqr.loc[(df_untrimmed_by_iqr[element] > self.get_lower_limit(df, columns)) & (df_untrimmed_by_iqr[element] < self.get_upper_limit(df, columns))]
        print('Number of trimmed outliers:', (len(df_untrimmed_by_iqr) - len(df_trimmed_by_iqr)))
        return df_trimmed_by_iqr

    def cap_by_limits(self, df, columns):
        df_uncapped = df.copy()
        for element in df[(columns)]:
            df_uncapped.loc[df_uncapped[element]>self.get_upper_limit(df, columns), element] = self.get_upper_limit(df, columns)
            df_uncapped.loc[df_uncapped[element]<self.get_lower_limit(df, columns), element] = self.get_lower_limit(df, columns)
            outliers = df_uncapped.loc[(df[element] < self.get_lower_limit(df, columns)) & (df[element] > self.get_upper_limit(df, columns))]
        df_capped_by_limits = df_uncapped
        print('Number of capped outliers', (len(df)-len(df_capped_by_limits)))
        return df_capped_by_limits

if __name__ == '__main__':
    pass