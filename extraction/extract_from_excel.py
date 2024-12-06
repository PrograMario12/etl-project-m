''' This module extracts data from an Excel file. '''
import pandas as pd
from interfaces.extractor import Extractor

class ExcelExtractor(Extractor):
    ''' This class extracts data from an Excel file. '''
    def __init__(self, file_path):
        ''' This method initializes the ExcelExtractor object. '''
        self.file_path = file_path

    def extract(self):
        ''' This method extracts data from an Excel file. '''
        return pd.read_excel(self.file_path)

    def validate(self):
        ''' This method validates the data extracted from an Excel file. '''
        assert self.file_path.endswith('.xlsx'), "File is not an Excel file."
        assert self.file_path, "File path is empty."
        assert self.file_path is not None, "File path is None."
        assert self.file_path, "File path does not exist."
        assert self.file_path, "File path is not a file."
        assert self.file_path, "File path is not readable."
