''' This module contains the Extractor class. '''
from abc import ABC, abstractmethod

class Extractor(ABC):
    ''' This class is an abstract class for extracting data. '''
    @abstractmethod
    def extract(self):
        ''' This method is an abstract method for extracting data. '''

    @abstractmethod
    def validate(self):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        print(f"Log: {message}")
