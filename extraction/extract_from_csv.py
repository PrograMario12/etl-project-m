''' This module extracts data from a CSV file. '''

import pandas as pd
from interfaces.extractor import Extractor

class CSVExtractor(Extractor):
    ''' This class extracts data from a CSV file. '''
    def __init__(self, file_path):
        ''' This method initializes the CSVExtractor object. '''
        self.file_path = file_path

    def extract(self):
        ''' This method extracts data from a CSV file. '''
        return pd.read_csv(self.file_path)

    def validate(self):
        ''' This method validates the data extracted from a CSV file. '''
        assert self.file_path.endswith('.csv'), "File is not a CSV file."
        assert self.file_path, "File path is empty."
        assert self.file_path is not None, "File path is None."
        assert self.file_path, "File path does not exist."
        assert self.file_path, "File path is not a file."
        assert self.file_path, "File path is not readable."
