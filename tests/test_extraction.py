""" This module contains tests for the extraction module. """
import unittest
from extraction.extract_from_csv import CSVExtractor
from extraction.extract_from_excel import ExcelExtractor

class TestCSVExtractor(unittest.TestCase):
    """ This class contains tests for the CSVExtractor class. """
    def setUp(self):
        self.extractor = CSVExtractor("../files_test/Netflix_Movies_and_TV_Shows.csv")

    def test_extract(self):
        """ This method tests the extract method of the CSVExtractor
        class. """
        data = self.extractor.extract()
        self.assertIsNotNone(data)

    def test_validate(self):
        """ This method tests the validate method of the
        CSVExtractor"""
        self.extractor.validate()

class TestExcelExtractor(unittest.TestCase):
    """ This class contains tests for the ExcelExtractor class. """
    def setUp(self):
        """ This method sets up the test. """
        self.extractor = ExcelExtractor("path/to/file.xlsx")

    def test_extract(self):
        """ This method tests the extract method of the 
        ExcelExtractor"""
        data = self.extractor.extract()
        self.assertIsNotNone(data)

    def test_validate(self):
        """ This method tests the validate method of the"""
        self.extractor.validate()

if __name__ == '__main__':
    unittest.main()
