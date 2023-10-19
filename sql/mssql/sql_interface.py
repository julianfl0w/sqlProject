import pymssql
import random
import string
import os
import sql_interface
from dotenv import load_dotenv


class SQLInterface:

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        self.MSSQL_SA_PASSWORD = os.getenv("MSSQL_SA_PASSWORD")
        print(self.MSSQL_SA_PASSWORD)
        self.server = "localhost"
        self.user = "sa" #sys admin
        self.password = self.MSSQL_SA_PASSWORD

        print("connecting to db")
        # Connect to the database with autocommit enabled
        self.conn = pymssql.connect(
            server=self.server, 
            user=self.user, 
            password=self.password, 
            autocommit=True
        )
        
        self.cursor = self.conn.cursor()


    def close(self):
        self.cursor.close()        
        self.conn.close()  # Close the connection when done
