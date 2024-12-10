import unittest
import pandas as pd
from transformation.clean_data import DataCleaner
from transformation.normalize_data import DataNormalizer
from transformation.aggregate_data import AggregateData

class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        self.cleaner = DataCleaner()
        self.df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})

    def test_transform(self):
        cleaned_df = self.cleaner.transform(self.df)
        self.assertFalse(cleaned_df.isnull().values.any())

    def test_validate(self):
        cleaned_df = self.cleaner.transform(self.df)
        self.cleaner.validate(cleaned_df)

class TestDataNormalizer(unittest.TestCase):

    def setUp(self):
        self.normalizer = DataNormalizer()
        self.df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

    def test_transform(self):
        normalized_df = self.normalizer.transform(self.df)
        self.assertAlmostEqual(normalized_df.mean().sum(), 0)
        self.assertAlmostEqual(normalized_df.std().sum(), normalized_df.shape[0])

    def test_validate(self):
        normalized_df = self.normalizer.transform(self.df)
        self.normalizer.validate(normalized_df)

class TestAggregateData(unittest.TestCase):

    def setUp(self):
        self.aggregator = AggregateData()
        self.df = pd.DataFrame({'id': [1, 1, 2], 'value': [10, 20, 30]})

    def test_transform(self):
        aggregated_df = self.aggregator.transform(self.df)
        self.assertEqual(aggregated_df.loc[1, 'value'], 30)
        self.assertEqual(aggregated_df.loc[2, 'value'], 30)

    def test_validate(self):
        aggregated_df = self.aggregator.transform(self.df)
        self.aggregator.validate(aggregated_df)

if __name__ == '__main__':
    unittest.main()