import pymssql
import keyboard
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
        self.setup_table()

    def setup_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
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
        cursor.close()

    @staticmethod
    def random_string(length=10):
        """Generate a random string of given length."""
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def perform_transaction(self):
        """Perform a random transaction on the database."""
        cursor = self.conn.cursor()

        try:
            # Generate random data
            description = self.random_string()
            amount = round(random.uniform(1, 1000), 2)  # random float between 1 and 1000

            # Insert transaction
            print(f"Inserting: {description}, ${amount}")
            cursor.execute("INSERT INTO Transactions (Description, Amount) VALUES (%s, %s)", (description, amount))

        except pymssql.Error as e:
            print(f"Error encountered: {e}")
            self.conn.rollback()

        finally:
            cursor.close()

    def run(self):
        print("Press 'a' to generate a random transaction. Press 'a' 10 times to exit.")

        press_count = 0

        while True:
            if keyboard.is_pressed('a'):
                self.perform_transaction()
                press_count += 1
                
                if press_count >= 10:
                    print("Pressed 'a' 10 times. Exiting...")
                    break

                while keyboard.is_pressed('a'):  # Prevent rapid firing by holding 'a'
                    pass

        self.conn.close()  # Close the connection when done

if __name__ == "__main__":
    transaction = Transaction()
    transaction.run()
