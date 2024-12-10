"""Unit tests for the transformation module."""
import unittest
import pandas as pd
import numpy as np
from transformation.clean_data import DataCleaner
from transformation.normalize_data import DataNormalizer
from transformation.aggregate_data import AggregateData

class TestDataCleaner(unittest.TestCase):
    """Unit tests for the DataCleaner class."""
    def setUp(self):
        """Initializes the DataCleaner object and a DataFrame."""
        self.cleaner = DataCleaner()
        self.df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})

    def test_transform(self):
        """Tests the transform method of the DataCleaner class."""
        cleaned_df = self.cleaner.transform(self.df)
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_validate(self):
        """Tests the validate method of the DataCleaner class."""
        cleaned_df = self.cleaner.transform(self.df)
        self.cleaner.validate(cleaned_df)

class TestDataNormalizer(unittest.TestCase):
    """Unit tests for the DataNormalizer class."""
    def setUp(self):
        # Crear una instancia de la clase Normalizer
        self.normalizer = DataNormalizer()

    def test_transform(self):
        """Tests the transform method of the DataNormalizer class."""
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        df = pd.DataFrame(data)

        normalized_df = self.normalizer.transform(df)

        expected_data = {
            'A': (df['A'] - df['A'].mean()) / df['A'].std(),
            'B': (df['B'] - df['B'].mean()) / df['B'].std(),
            'C': (df['C'] - df['C'].mean()) / df['C'].std()
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(normalized_df, expected_df)

    def test_transform_empty_dataframe(self):
        """ Tests the transform method with an empty DataFrame. """
        df = pd.DataFrame()

        normalized_df = self.normalizer.transform(df)

        self.assertTrue(normalized_df.empty)

    def test_transform_single_value(self):
        """ Tests the transform method with a DataFrame with a single value. """
        data = {'A': [1]}
        df = pd.DataFrame(data)

        normalized_df = self.normalizer.transform(df)

        self.assertTrue(np.isnan(normalized_df['A'][0]))

    def test_validate_normalized_data(self):
        """Tests the validate method of the DataNormalizer class."""
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        df = pd.DataFrame(data)

        # Aplicar la normalización
        normalized_df = self.normalizer.transform(df)

        # Validar el DataFrame normalizado
        self.normalizer.validate(normalized_df)

    def test_validate_non_normalized_data(self):
        """Tests the validate method with non-normalized data."""
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        df = pd.DataFrame(data)

        with self.assertRaises(AssertionError):
            self.normalizer.validate(df)

    def test_validate_with_missing_values(self):
        """Tests the validate method with missing values."""   
        data = {
            'A': [1, 2, np.nan, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500]
        }
        df = pd.DataFrame(data)

        # Aplicar la normalización
        normalized_df = self.normalizer.transform(df.fillna(df.mean()))

        # Introducir un valor nulo manualmente
        normalized_df.iloc[2, 0] = np.nan

        # Verificar que la validación falle para datos con valores nulos
        with self.assertRaises(AssertionError):
            self.normalizer.validate(normalized_df)

class TestAggregateData(unittest.TestCase):
    """Unit tests for the AggregateData class."""
    def setUp(self):
        """Initializes the AggregateData object and a DataFrame."""
        self.aggregator = AggregateData()
        self.df = pd.DataFrame({'id': [1, 1, 2], 'value': [10, 20, 30]})

    def test_transform(self):
        """Tests the transform method of the AggregateData class."""
        aggregated_df = self.aggregator.transform(self.df)
        self.assertEqual(aggregated_df.loc[1, 'value'], 30)
        self.assertEqual(aggregated_df.loc[2, 'value'], 30)

    def test_validate(self):
        """Tests the validate method of the AggregateData class."""
        aggregated_df = self.aggregator.transform(self.df)
        print(aggregated_df)
        self.aggregator.validate(aggregated_df)

if __name__ == '__main__':
    unittest.main()
