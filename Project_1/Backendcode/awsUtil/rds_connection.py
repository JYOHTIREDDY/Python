"""
Module: rds_connection.py

This module contains functions for retrieving
database credentials from AWS Secrets Manager
and connecting to a PostgreSQL database using
the psycopg2 library.
"""
import json
import boto3
import psycopg2


def get_secret(secret_name):
    """
    Retrieve the secret with the provided name
    from AWS Secrets Manager.
    """
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager'
        )


    try:
        response = client.get_secret_value(
            SecretId=secret_name
            )
    except Exception as err:
        raise err
    else:
        if 'SecretString' in response:
            secret = json.loads(
                response['SecretString']
                )
            return secret
        else:
            raise ValueError(
                "SecretString not found in theresponse from AWS Secrets Manager."
                )


def connect_to_postgres(credentials):
    """
    Connect to PostgreSQL using the provided
    credentials.
    """
    #in this function as of now I'm expecting
    # the host, port , dbname, username, password, database name in the secrets manager in AWS
    try:
        conn = psycopg2.connect(
            host=credentials['host'],
            port=credentials['port'],
            user=credentials['username'],
            password=credentials['password'],
            database='IONE'
        )
        return conn
    except Exception as err:
        raise err
