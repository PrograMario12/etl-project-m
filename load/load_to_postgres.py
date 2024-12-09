''' This module is responsible for loading the data into the 
Postgres database. '''
from interfaces.loader import Loader
from database.connection import DatabaseConnection
from database.commiter import DatabaseCommiter

class PostgresLoader(Loader):
    ''' This class is responsible for loading the data into the
    Postgres database. '''
    def __init__(self, table_name):
        ''' This method initializes the loader. '''
        self.table_name = table_name
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.commiter = DatabaseCommiter(self.connection)

    def load(self, df):
        ''' This method loads the data into the Postgres database. '''
        df.to_sql(self.table_name, self.connection, if_exists='replace', index=False)
        self.commiter.commit()
        self.connection.disconnect()

    def validate_connection(self):
        ''' This method validates the connection. '''
        return self.connection.is_connected()
