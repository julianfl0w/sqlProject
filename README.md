# sqlProject
A review of available SQL and NoSQL Databases


## Requirements
- Docker
- Python

## Windows (Additional)
- WSL
- Docker Desktop
- SQL Server Management Studio (SSMS)

## Instructions

### SQL 
- Open Docker Desktop (Windows only)
- Open SQL Server Management Studio (SSMS)
- Go to sql/mssql in this repo
- Create a .env file here with the following format
```bash
# Acceptance of Microsoft's EULA for SQL Server
ACCEPT_EULA=Y
# Password for the 'sa' user for SQL Server
MSSQL_SA_PASSWORD='Passw0rd!'
```
- Run python runDocker.py. This will start the MSSQL DB
- Connect to MSSQL DB with SSMS using account "sa", password as given in the .env, and Server Name "localhost"
- run python create_transaction.py
- refresh the SSMS connection. see that your data is there!