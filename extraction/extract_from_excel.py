"""
This module extracts data from an Excel file.

This module provides the ExcelExtractor class which extracts and validates data from an Excel file.
"""
import os
import pandas as pd
from interfaces.extractor import Extractor

class ExcelExtractor(Extractor):
    """Extracts data from an Excel file.

    This class provides methods to extract and validate data from an Excel file.
    """
    def __init__(self, file_path):
        """ This method initializes the ExcelExtractor object. """
        self.file_path = file_path

    def extract(self):
        """ This method extracts data from an Excel file. """
        return pd.read_excel(self.file_path)

    def validate(self):
        """ This method validates the data extracted from an Excel 
        file. """
        assert self.file_path.endswith('.xlsx'), (
            """File is not an Excel file. Please provide a file with a .xlsx
            extension."""
        )
        assert self.file_path.endswith('.xlsx'), (
            f"""File '{self.file_path}' is not an Excel file.
            Please provide a file with a .xlsx extension."""
        )
        assert os.path.isfile(self.file_path), (
            f"""File path '{self.file_path}' does not exist or is not a file.
            Please provide a valid file path."""
        )
        assert os.access(self.file_path, os.R_OK), (
            f"""File '{self.file_path}' is not readable. 
            Please check the file permissions."""
        )
