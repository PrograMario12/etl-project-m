''' This module contains the classes for database connection. '''
from abc import ABC, abstractmethod
import logging
import psycopg2
import config

logging.basicConfig(level=logging.INFO)

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
    '''
    This class is a concrete class for connecting to the database.

    This class provides methods to connect to and disconnect from a
    PostgreSQL database using the psycopg2 library.
    It also includes a method to check if the connection is currently
    established.

    Usage:
        db_connection = DatabaseConnection()
        db_connection.connect()
        if db_connection.is_connected():
            print("Connection is established")
        db_connection.disconnect()
    '''
    def __init__(self):
        ''' This method initializes the database connection. '''
        self.connection = None
        self.cursor = None

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
            logging.info("Connected to database")

        except psycopg2.OperationalError as e:
            logging.error("Operational error connecting to database: %s", e)
        except psycopg2.DatabaseError as e:
            logging.error("Database error connecting to database: %s", e)

    def disconnect(self):
        ''' This method disconnects from the database. '''
        if self.connection:
            self.connection.close()
            logging.info("Disconnected from database")
        else:
            logging.info("No connection to close")

    def commit(self):
        ''' This method commits a transaction. '''
        try:
            self.connection.commit()
            logging.info("Transaction committed")
        except self.connection.DatabaseError as e:
            logging.error("Database error committing transaction: %s", e)

    def is_connected(self):
        ''' This method checks if the connection is established. '''
        return self.connection is not None and self.connection.closed == 0
