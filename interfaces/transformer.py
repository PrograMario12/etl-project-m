""" This module contains the Transformer class. """
from abc import ABC, abstractmethod

class Transformer(ABC):
    """
    This class is an abstract base class for transforming data.

    The Transformer class provides a template for creating data transformation
    and validation methods. Subclasses must implement the `transform` and 
    `validate` methods to define specific transformation and validation logic.

    Methods:
        - transform(dataframe): Abstract method to transform the data.
        - validate(dataframe): Abstract method to validate the data.
        - log(message): Logs a message to the console.
    """
    @abstractmethod
    def transform(self, dataframe):
        ''' This method is an abstract method for transforming data. '''

    @abstractmethod
    def validate(self, dataframe):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        print(f"Log: {message}")
