import pymssql
import random
import string
import os
from dotenv import load_dotenv

class Transaction:

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        self.MSSQL_SA_PASSWORD = os.getenv("MSSQL_SA_PASSWORD")
        print(self.MSSQL_SA_PASSWORD)
        self.server = "localhost"
        self.user = "sa"
        self.password = self.MSSQL_SA_PASSWORD

        # Connect to the database with autocommit enabled
        self.conn = pymssql.connect(
            server=self.server, 
            user=self.user, 
            password=self.password, 
            autocommit=True
        )
        
        self.cursor = self.conn.cursor()
        self.setup_table()

    def setup_table(self):
        print("Creating Table")
        self.cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Transactions')
            BEGIN
                CREATE TABLE Transactions
                (
                    ID INT PRIMARY KEY IDENTITY(1,1),
                    Description NVARCHAR(255),
                    Amount DECIMAL(10, 2)
                );
            END
        """)

    @staticmethod
    def random_string(length=10):
        """Generate a random string of given length."""
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def perform_transaction(self):
        """Perform a random transaction on the database."""

        # Generate random data
        description = self.random_string()
        amount = round(random.uniform(1, 1000), 2)  # random float between 1 and 1000

        # Insert transaction
        print(f'Inserting: {description}, {amount}')
        self.cursor.execute("INSERT INTO Transactions (Description, Amount) VALUES (%s, %s)", (description, amount))

    def close(self):
        self.cursor.close()        
        self.conn.close()  # Close the connection when done

    def run(self):

        press_count = 0

        while True:
           # input(f"Enter to send transaction {press_count}")
            self.perform_transaction()
            press_count += 1
            
            if press_count >= 3:
                print("Pressed 'a' 10 times. Exiting...")
                break
        self.close()

if __name__ == "__main__":
    transaction = Transaction()
    transaction.run()
