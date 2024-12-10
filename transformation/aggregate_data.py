"""
This module provides functionality to aggregate and validate data.

Classes:
    AggregateData: Inherits from Transformer and provides methods to 
                   aggregate and validate data.

Methods:
    transform(dataframe): Aggregates data by grouping by 'id' and summing.
    validate(dataframe, expected_sum=1000): Validates the aggregated data 
                                            against several conditions.
"""
from interfaces.transformer import Transformer

class AggregateData(Transformer):
    """ This class aggregates data. """
    def transform(self, dataframe):
        """
        This method aggregates data by grouping the dataframe by 'id'
        and summing the values.
        """
        return dataframe.groupby('id').sum()

    def validate(self, dataframe):
        """ This method validates the aggregated data. """
        if 'value' not in dataframe.columns:
            raise ValueError("Data is not aggregated correctly.")
        if dataframe.index.name != 'id':
            raise ValueError("Data is not indexed by id.")
