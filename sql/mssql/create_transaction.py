import pymssql
import random
import string
import os
import sql_interface
from dotenv import load_dotenv

class Transaction(sql_interface.SQLInterface):
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

    def run(self):
        self.setup_table()
        press_count = 0

        for i in range(1000):
           # input(f"Enter to send transaction {press_count}")
            self.perform_transaction()
        self.close()

if __name__ == "__main__":
    transaction = Transaction()
    transaction.run()
