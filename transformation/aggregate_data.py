"""  This module aggregates data. """
from interfaces.transformer import Transformer

class AggregateData(Transformer):
    """ This class aggregates data. """
    def transform(self, dataframe):
        """ This method aggregates data. """
        return dataframe.groupby('id').sum()

    def validate(self, dataframe, expected_sum=1000):
        """ This method validates the aggregated data. """
        assert dataframe.shape[0] == 100, "Data is not aggregated."
        assert dataframe.isnull().sum().sum() == 0, "Data still has missing values."
        assert dataframe.sum().sum() == 1000, "Data is not aggregated correctly."
        assert dataframe.index.name == 'id', "Data is not indexed by id."
        assert 'value' in dataframe.columns, "Data is not aggregated correctly."
