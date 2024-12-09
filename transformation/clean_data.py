"""
This module cleans data by removing rows with missing values.
It provides a DataCleaner class that inherits from Transformer.
The DataCleaner class has methods to transform and validate the data.
"""
from interfaces.transformer import Transformer

class DataCleaner(Transformer):
    """ This class cleans data. """
    def transform(self, dataframe):
        """
        This method cleans data by removing rows with missing values.

        Parameters:
        dataframe): (DataFrame): The input data frame to be cleaned.

        Returns:
        DataFrame: The cleaned data frame with rows containing missing
        values removed.
        """
        return dataframe.dropna()

    def validate(self, dataframe):
        """ This method validates the cleaned data. """
        assert dataframe.isnull().sum().sum() == 0, \
            "Validation failed: Data still has missing values."
