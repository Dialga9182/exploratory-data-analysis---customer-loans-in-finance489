import missingno as msno
from scipy.stats import skew, yeojohnson
from matplotlib import pyplot as plt
import seaborn as sns


class Plotter:
    """Plot things using seaborn.
    """    
    
    def __init__(self):
        """Initialise.
        """
        pass
    
    def generate_a_plot_for_nulls(self, df):
        """Generate a plot for nulls.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        msno.matrix(df)
        return df
    
    def skew_correction(self, df):
        """Correct the skew on a dataframe.

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
        """
        list_for_skew = ['loan_amount', 'funded_amount', 'funded_amount_inv', 'instalment', 'open_accounts', 'total_accounts','out_prncp','out_prncp_inv', 'total_payment', 'total_payment_inv', 'total_rec_prncp', 'total_rec_int', 'last_payment_amount']
        for element in list_for_skew:
            print(element)
            print(skew(df[element]))

        for column in list_for_skew: 
           df[column], _ = yeojohnson(df[column])

        df[['loan_amount', 'funded_amount', 'funded_amount_inv', 'instalment',
        'open_accounts', 'total_accounts', 'out_prncp', 'out_prncp_inv',
        'total_payment', 'total_payment_inv', 'total_rec_prncp',
        'total_rec_int', 'last_payment_amount']].hist(figsize=(20,15))
        return df
    
    def plotting_outliers(self, df):
        """Plot outliers.

        Args:
            df (_type_): _description_
        """
        pass
    
    def plot_boxplots(self, df, columns):
        """Plot boxplots.

        Args:
            df (_type_): _description_
            columns (_type_): _description_
        """
        plt.figure(figsize=(15, 8))

        for element, col in enumerate(columns, 1):
            plt.subplot(1, len(columns), element)
            sns.boxplot(y=df[col])
            plt.title(f'Boxplot of {col}')
            plt.ylabel(col)
        plt.tight_layout()
        plt.show()
        #print('original boxplots')

if __name__ == '__main__':
    pass