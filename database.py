''' This module contains the classes for database connection, query 
execution and commiting transaction. '''
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

class QueryExecutor(ABC):
    ''' This class is an abstract class for executing queries. '''
    @abstractmethod
    def execute_query(self, query):
        ''' This method is an abstract method for executing a
        query. '''

    @abstractmethod
    def fetch_results(self):
        ''' This method is an abstract method for fetching the
        results of the query. '''

class Commiter(ABC):
    ''' This class is an abstract class for commiting
    transactions. '''
    @abstractmethod
    def commit(self):
        ''' This method is an abstract method for commiting'''

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

class DatabaseQueryExecutor(QueryExecutor):
    ''' This class is a concrete class for executing queries. '''

    def __init__(self, connection):
        ''' This method initializes the query executor. '''
        self.connection = connection
        self.cursor = None

    def execute_query(self, query):
        ''' This method executes a query. '''
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute(query)
            print("Query executed successfully")
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_results(self):
        ''' This method fetches the results of the query. '''
        try:
            results = self.cursor.fetchall()
            print("Results fetched successfully")
            return results
        except Exception as e:
            print(f"Error fetching results: {e}")
            return None

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

class ConnectionValidator:
    ''' This class validates the connection. '''
    def __init__(self, connection):
        ''' This method initializes the connection validator. '''
        self.connection = connection

    def validate(self):
        ''' This method validates the connection. '''
        if self.connection.is_connected():
            print("Connection is valid")
        else:
            print("Connection is invalid")

if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.connect()

    validator = ConnectionValidator(db_connection)
    validator.validate()

    query_executor = DatabaseQueryExecutor(db_connection.connection)
    query_executor.execute_query("SELECT * FROM sch_dev.registers limit 10")
    results = query_executor.fetch_results()
    if results:
        for result in results:
            print(result)

    db_connection.disconnect()
    validator.validate()
