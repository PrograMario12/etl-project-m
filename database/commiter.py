''' This module contains the classes for commiting transactions. '''
from abc import ABC, abstractmethod

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

class DatabaseCommiter(Commiter):
    ''' This class is a concrete class for commiting transactions. '''

    def __init__(self, connection):
        ''' This method initializes the commiter. '''
        self.connection = connection

    def commit(self):
        ''' This method commits a transaction. '''
        try:
            self.connection.commit()
            print("Transaction commited")
        except Exception as e:
            print(f"Error commiting transaction: {e}")

    def validate_connection(self):
        ''' This method validates the connection. '''
        if self.connection.is_connected():
            print("Connection is established")
        else:
            print("Connection is not established")
