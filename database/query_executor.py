""" This module contains the QueryExecutor abstract class and the
DatabaseQueryExecutor concrete class. """
from abc import ABC, abstractmethod
import logging
import psycopg2

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class QueryExecutor(ABC):
    """ This class is an abstract class for executing queries. """
    @abstractmethod
    def execute_query(self, query):
        """
        This method is an abstract method for executing a query.
        """

    @abstractmethod
    def fetch_results(self):
        """
        This method is an abstract method for fetching the
        results of the query.
        """

class DatabaseQueryExecutor(QueryExecutor):
    """ This class is a concrete class for executing queries. """

    def __init__(self, connection):
        """ This method initializes the query executor. """
        self.connection = connection
        self.cursor = None

    def execute_query(self, query):
        """ This method executes a query. """
        if not self.connection.is_connected():
            logging.error("Cannot execute query: No connection to the database.")
            return

        try:
            self.cursor = self.connection.connection.cursor()
            self.cursor.execute(query)
            logging.info("Query executed successfully")
        except psycopg2.Error as e:
            logging.error("Database error: %s", e)
            self.cursor = None
        except AttributeError as e:
            logging.error("Unexpected error: %s", e)

    def fetch_results(self):
        """ This method fetches the results of the query. """
        if self.cursor is None:
            logging.error("Error: No query has been executed.")
            return None
        try:
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            logging.error("Error fetching results: %s", e)
            return None

    def close_cursor(self):
        """ This method closes the cursor. """
        if self.cursor is not None:
            self.cursor.close()
