""" This module contains the tests for the DatabaseCommiter class. """
import unittest
from database.connection import DatabaseConnection
from database.commiter import DatabaseCommitter

class TestDatabaseCommiter(unittest.TestCase):
    """ This class contains the tests for the DatabaseCommiter
    class. """
    def setUp(self):
        """
        This method sets up the DatabaseCommiter instance.
        """
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.commiter = DatabaseCommitter(self.connection)

    def tearDown(self):
        """
        This method disconnects the DatabaseCommiter instance.
        """
        self.connection.disconnect()

    def test_execute_commit(self):
        """
        This method tests the execute_commit method.
        """
        self.commiter.commit()
