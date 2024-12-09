''' This module contains the classes for database connection. '''
from abc import ABC, abstractmethod
import psycopg2
import config

class Connection(ABC):
    ''' This class is an abstract class for database connection. '''
    @abstractmethod
    def connect(self):
        ''' This method is an abstract method for connecting to the
        database. '''

    @abstractmethod
    def disconnect(self):
        ''' This method is an abstract method for disconnecting from
        the database. '''

    @abstractmethod
    def is_connected(self):
        ''' This method is an abstract method for checking if the
        connection is established. '''

class DatabaseConnection(Connection):
    ''' This class is a concrete class for connecting to the 
    database. '''
    def __init__(self):
        ''' This method initializes the database connection. '''
        self.connection = None

    def connect(self):
        ''' This method connects to the database. '''
        try:
            self.connection = psycopg2.connect(
                user=config.USER,
                password=config.PASSWORD,
                host=config.HOST,
                port=config.PORT,
                database=config.DATABASE
            )
            print("Connected to database")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        ''' This method disconnects from the database. '''
        if self.connection:
            self.connection.close()
            print("Disconnected from database")
        else:
            print("No connection to disconnect")

    def is_connected(self):
        ''' This method checks if the connection is established. '''
        return self.connection is not None
