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

    def validate(self, dataframe, expected_sum=1000):
        """ This method validates the aggregated data. """
        assert 'value' in dataframe.columns, "Data is not aggregated correctly."
        assert dataframe.index.name == 'id', "Data is not indexed by id."
        assert dataframe.sum().sum() == expected_sum, (
            f"Data is not aggregated correctly. Expected sum: {expected_sum}."
        )
        raise ValueError("Data is not aggregated correctly.")
