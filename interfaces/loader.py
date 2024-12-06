''' This module contains the Loader class. '''
from abc import ABC, abstractmethod

class Loader(ABC):
    ''' This class is an abstract class for loading data. '''
    @abstractmethod
    def load(self, df):
        ''' This method is an abstract method for loading data. '''

    @abstractmethod
    def validate(self, df):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        print(f"Log: {message}")
