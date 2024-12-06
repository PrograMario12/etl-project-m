''' This module contains the Transformer class. '''
from abc import ABC, abstractmethod

class Transformer(ABC):
    ''' This class is an abstract class for transforming data. '''
    @abstractmethod
    def transform(self, df):
        ''' This method is an abstract method for transforming data. '''

    @abstractmethod
    def validate(self, df):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        print(f"Log: {message}")
