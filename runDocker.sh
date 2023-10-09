#!/bin/bash

# Source the .env file
source .env

echo $MSSQL_SA_PASSWORD

# Run the Docker command using the environment variables
docker run \
    --rm \
    -e "ACCEPT_EULA=$ACCEPT_EULA" \
    -e MSSQL_SA_PASSWORD=$MSSQL_SA_PASSWORD \
    -p 1433:1433 \
    --name sqlpreview \
    --hostname sqlpreview \
    mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04
