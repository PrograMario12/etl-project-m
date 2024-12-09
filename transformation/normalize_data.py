""" This module normalizes data. """
import numpy as np
from interfaces.transformer import Transformer


class DataNormalizer(Transformer):
    '''
    This class normalizes data by centering and scaling it.
    Methods:
        transform(df): Normalizes the data by subtracting the mean and
            dividing by the standard deviation.
        validate(df): Validates that the data is centered, scaled, and
          has no missing values.
        epsilon = 1e-8  # small constant to avoid division by zero
        return (df - df.mean()) / (df.std() + epsilon)
    Usage:
        normalizer = DataNormalizer()
        normalized_df = normalizer.transform(df)
        normalizer.validate(normalized_df)
    '''
    def transform(self, df):
        '''
        This method normalizes data.
        Parameters:
            df (DataFrame): The input data frame to be normalized.

        Returns:
            DataFrame: The normalized data frame.
        '''
        return (df - df.mean()) / df.std()

    def validate(self, df):
        assert np.isclose(df.std().sum(), df.shape[0]), "Data is not scaled."
        assert df.mean().sum() == 0, "Data is not centered."
        assert df.std().sum() == df.shape[0], "Data is not scaled."
        assert df.isnull().sum().sum() == 0, "Data still has missing values."
