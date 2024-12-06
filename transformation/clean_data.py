''' This module cleans data. '''
from interfaces.transformer import Transformer

class DataCleaner(Transformer):
    ''' This class cleans data. '''
    def transform(self, df):
        ''' This method cleans data. '''
        return df.dropna()

    def validate(self, df):
        ''' This method validates the cleaned data. '''
        assert df.isnull().sum().sum() == 0, "Data still has missing values."
