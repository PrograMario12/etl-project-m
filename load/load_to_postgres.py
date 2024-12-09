""" This module is responsible for loading the data into the 
Postgres database. """
from interfaces.loader import Loader
from database.connection import DatabaseConnection
from database.commiter import DatabaseCommiter

class PostgresLoader(Loader):
    """ This class is responsible for loading the data into the
    Postgres database. """
    def __init__(self, table_name):
        '''
        This method initializes the loader.

        Parameters:
        table_name (str): The name of the table where data will be loaded.
        '''

        self.connection = DatabaseConnection()
        self.connection.connect()
        self.table_name = table_name
        self.commiter = DatabaseCommiter(self.connection)

    def load(self, df):
        ''' This method loads the data into the Postgres database. '''
        df.to_sql(self.table_name,
                  self.connection,
                  if_exists='replace',
                  index=False
                  )
        self.commiter.commit()
        self.connection.disconnect()

    def validate_connection(self):
        ''' This method validates the connection. '''
        return self.connection.is_connected()
