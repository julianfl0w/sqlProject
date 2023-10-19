import os
import subprocess
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Print the MSSQL_SA_PASSWORD
# print(os.environ["MSSQL_SA_PASSWORD"])

# Run the Docker command using the environment variables
command = [
    "docker", "run",
    "--rm",
    "-e", f"ACCEPT_EULA={os.environ['ACCEPT_EULA']}",
    "-e", f"SA_PASSWORD={os.environ['MSSQL_SA_PASSWORD']}",
    "-p", "1433:1433",
    "--name", "sqlpreview",
    "--hostname", "sqlpreview",
    "mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04"
]

subprocess.run(command)
