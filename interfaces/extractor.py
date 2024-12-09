""" This module contains the Extractor class. """
from abc import ABC, abstractmethod

class Extractor(ABC):
    """
    This class is an abstract base class for extracting data.
    
    Responsibilities:
    - Define the interface for data extraction by implementing the
    `extract` method.
    - Ensure data validity by implementing the `validate` method.
    - Provide a logging mechanism through the `log` method.

    Intended Usage:
    - Subclass this class and implement the `extract` and `validate`
    methods to create a concrete data extractor.
    - Use the `log` method to log messages during the extraction 
    process.
    """

    @abstractmethod
    def extract(self):
        ''' This method is an abstract method for extracting data. '''

    @abstractmethod
    def validate(self):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        print(f"Log: {message}")
