""" This module contains the unit tests for the DatabaseQueryExecutor
class. """

import unittest
from database.connection import DatabaseConnection
from database.query_executor import DatabaseQueryExecutor

class TestDatabaseQueryExecutor(unittest.TestCase):
    """ This class contains the tests for the DatabaseQueryExecutor
    class. """
    def setUp(self):
        """
        This method sets up the DatabaseQueryExecutor instance.
        """
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.query_executor = DatabaseQueryExecutor(self.connection)

    def tearDown(self):
        """
        This method disconnects the DatabaseQueryExecutor instance.
        """
        self.connection.disconnect()
        self.query_executor.close_cursor()

    def test_execute_query(self):
        """
        This method tests the execute_query method.
        """
        self.query_executor.execute_query("SELECT 1")
        results = self.query_executor.fetch_results()
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
