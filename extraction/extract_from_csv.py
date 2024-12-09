"""
This module provides functionality to extract and validate data from a CSV file.

Classes:
    CSVExtractor: A class to extract and validate data from a CSV file.

Usage example:
    extractor = CSVExtractor('path/to/your/file.csv')
    data = extractor.extract()
    extractor.validate()
"""

import os
import pandas as pd
from interfaces.extractor import Extractor

class CSVExtractor(Extractor):
    ''' This class extracts data from a CSV file. '''
    def __init__(self, file_path):
        ''' This method initializes the CSVExtractor object. '''
        self.file_path = file_path

    def extract(self):
        ''' This method extracts data from a CSV file. '''
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            ) from exc
        except pd.errors.EmptyDataError as exc:
            raise ValueError(f"No data: {self.file_path} is empty") from exc
        except pd.errors.ParserError as exc:
            raise ValueError(
                f"Parsing error: {self.file_path} is not a valid CSV"
            ) from exc
        except Exception as exc:
            raise RuntimeError(
                f"An error occurred while reading {self.file_path}: {exc}"
            ) from exc

    def validate(self):
        ''' This method validates the data extracted from a CSV file. '''
        self._validate_file_path()

    def _validate_file_path(self):
        ''' This helper method validates the file path. '''
        assert self.file_path, "File path is empty or None."
        assert self.file_path.endswith('.csv'), "File is not a CSV file."
        assert os.path.exists(self.file_path), "File path does not exist."
        assert os.path.isfile(self.file_path), "File path is not a file."
        assert os.access(self.file_path, os.R_OK), "File path is not readable."
