""" This module contains the tests for the DatabaseConnection class. """
import unittest
from database.connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    """ This class contains the tests for the DatabaseConnection class"""
    def test_connect(self):
        """ This method tests the connect method. """
        db_connection = DatabaseConnection()
        db_connection.connect()
        self.assertTrue(db_connection.is_connected())
        db_connection.disconnect()
        self.assertFalse(db_connection.is_connected())

    def test_disconnect(self):
        """ This method tests the disconnect method. """
        db_connection = DatabaseConnection()
        db_connection.connect()
        db_connection.disconnect()
        self.assertFalse(db_connection.is_connected())

    def test_is_connected(self):
        """ This method tests the is_connected method. """
        db_connection = DatabaseConnection()
        self.assertFalse(db_connection.is_connected())

if __name__ == '__main__':
    unittest.main()
