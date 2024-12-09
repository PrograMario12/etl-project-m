''' This module contains the classes for commiting transactions. '''
from abc import ABC, abstractmethod
import logging

class Commiter(ABC):
    ''' This class is an abstract class for commiting
    transactions. '''
    @abstractmethod
    def commit(self):
        ''' This method is an abstract method for commiting'''

    @abstractmethod
    def validate_connection(self):
        ''' This method is an abstract method for validating the
        connection. '''

class DatabaseCommitter(Commiter):
    ''' This class is a concrete class for commiting transactions. '''

    def __init__(self, connection):
        '''
        Initializes the DatabaseCommiter with a database connection.

        Parameters:
        connection (object): The database connection object.
        '''
        self.connection = connection

    def commit(self):
        ''' This method commits a transaction. '''
        try:
            self.connection.commit()
            logging.info("Transaction committed")
        except self.connection.DatabaseError as e:
            logging.error("Database error committing transaction: %s", e)

    def validate_connection(self):
        ''' This method validates the connection. '''
        if self.connection.is_connected():
            logging.info("Connection is established")
        else:
            logging.error("Connection is not established")
