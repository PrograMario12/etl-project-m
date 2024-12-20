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
import logging
import pandas as pd
from interfaces.extractor import Extractor

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

class CSVExtractor(Extractor):
    ''' This class extracts data from a CSV file. '''
    def __init__(self, file_path, encoding='utf-8'):
        ''' This method initializes the CSVExtractor object. '''
        self.file_path = os.path.abspath(file_path)
        self.encoding = encoding

    def extract(self):
        ''' This method extracts data from a CSV file. '''
        try:
            logging.info("Extracting data from %s", self.file_path)
            data = pd.read_csv(self.file_path, encoding=self.encoding)
            logging.info("Data extracted successfully")
            return data
        except FileNotFoundError as exc:
            logging.error("File not found: %s", self.file_path)
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            ) from exc
        except pd.errors.EmptyDataError as exc:
            logging.error("No data: %s is empty", self.file_path)
            raise ValueError(f"No data: {self.file_path} is empty") from exc
        except pd.errors.ParserError as exc:
            logging.error(
                "Parsing error: %s is not a valid CSV",
                self.file_path
                )
            raise ValueError(
                f"Parsing error: {self.file_path} is not a valid CSV"
            ) from exc
        except UnicodeDecodeError as exc:
            logging.error(
                "Encoding error: %s cannot be decoded with %s",
                self.file_path,
                self.encoding
                )
            logging.info("Attempting to read the file with 'latin1' encoding")
            try:
                data = pd.read_csv(self.file_path, encoding='latin1')
                logging.info("""Data extracted successfully with 'latin1'
                    encoding""")
                return data
            except Exception as exc_inner:
                logging.error(
                    """An error occurred while reading %s with 'latin1'
                    encoding: %s""",
                    self.file_path, exc_inner)
                raise ValueError(
                    f"""Encoding error: {self.file_path} cannot be decoded with
                    {self.encoding} or 'latin1'"""
                ) from exc_inner

    def validate(self):
        ''' This method validates the data extracted from a CSV file. '''
        is_ok = self._validate_file_path()
        return is_ok

    def _validate_file_path(self):
        ''' This helper method validates the file path. '''
        if not self.file_path:
            return "File path is empty or None."
        if not self.file_path.endswith('.csv'):
            return "File path is not a CSV file."
        if not os.path.exists(self.file_path):
            return "File path does not exist."
        if not os.path.isfile(self.file_path):
            return "File path is not a file."
        if not os.access(self.file_path, os.R_OK):
            return "File path is not readable."

        return True
