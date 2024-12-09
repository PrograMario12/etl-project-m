''' This module contains the Loader class. '''
import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Loader(ABC):
    """
    This class is an abstract class for loading data.

    Intended use:
    - Subclass this abstract class to implement specific data loading mechanisms.
    - Implement the 'load' method to define how data should be loaded.
    - Implement the 'validate' method to define how data should be validated before loading.

    Important notes:
    - This class should not be instantiated directly.
    - Use the 'log' method to log messages during the loading process.
    """

    @abstractmethod
    def load(self, df):
        ''' This method is an abstract method for loading data. '''

    @abstractmethod
    def validate(self, df):
        ''' This method is an abstract method for validating data. '''

    def log(self, message):
        ''' This method logs the message. '''
        logging.info(message)
