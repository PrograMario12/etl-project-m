""" This module contains tests for the extraction module. """
import unittest
import os
from extraction.extract_from_csv import CSVExtractor
from extraction.extract_from_excel import ExcelExtractor

class TestCSVExtractor(unittest.TestCase):
    """ This class contains tests for the CSVExtractor class. """
    def setUp(self):
        file_path = os.path.join(os.path.dirname(__file__),
                                "../files_test/Netflix_Movies_and_TV_Shows.csv"
                                )
        self.extractor = CSVExtractor(file_path=file_path)

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
        file_path = os.path.join(os.path.dirname(__file__),
                            "../files_test/Netflix_Movies_and_TV_Shows.xlsx"
                        )
        self.extractor = ExcelExtractor(file_path=file_path)

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
