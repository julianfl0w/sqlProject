from dotenv import load_dotenv
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

class DatabaseHistogram:

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        self.MSSQL_SA_PASSWORD = os.getenv("MSSQL_SA_PASSWORD")
        self.server = "localhost"
        self.user = "sa" #sys admin
        self.password = self.MSSQL_SA_PASSWORD

        print("connecting to db")
        # Connect to the database with SQLAlchemy
        self.engine = create_engine(
            f'mssql+pymssql://{self.user}:{self.password}@{self.server}'
        )

    def plot_histogram(self, data, bins=30):
        print("plotting")
        sns.histplot(data, bins=bins, kde=True)
        plt.xlabel('Amount')
        plt.ylabel('Frequency')
        plt.title('Histogram of Amount')
        plt.show()

    def run(self, query):
        data = pd.read_sql(query, self.engine)
        self.plot_histogram(data['Amount'])

if __name__ == "__main__":
    query = """
    SELECT Amount
    FROM Transactions
    """
    db_hist = DatabaseHistogram()
    db_hist.run(query)
