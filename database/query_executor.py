''' This module contains the QueryExecutor abstract class and the
DatabaseQueryExecutor concrete class. '''
from abc import ABC, abstractmethod

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
