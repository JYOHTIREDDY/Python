"""
This test class is used to create a 
connction object using Psycopy2 libray and 
get secret from the AWS secret Manager.
"""
import os
import sys
import json
import unittest




# Determine the directory path of the project root directory
dir_rb = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the code directory to the system path
code_dir = os.path.join(dir_rb, 'code')
sys.path.insert(0, code_dir)

# Now you should be able to import from awsUtil package
from Project_1.Backendcode.awsUtil.rds_connection import connect_to_postgres, get_secret




class CustomError(Exception):
    """
    This class is used to throw the custom exception
    """
    pass


class TestDatabaseFunctions(unittest.TestCase):
    """
    This is the main test class for testing connection 
    and secret manager functionality
    """
    @patch('boto3.session.Session.client')
    def test_get_secret_valid_secret(self, mock_boto3_client):
        """
        This method is used to test postive scenrios 
        for get the client object from Boto3 library 
        to get connect AWS secret manager
        """
        secret_name = "test-secret"
        expected_secret = {"username": "test-user", 
                           "password": "test_password"}
        mock_boto3_client.return_value.get_secret_value.return_value = {
            "SecretString": json.dumps(expected_secret)
        }
        actual_secret = get_secret(secret_name)
        self.assertEqual(actual_secret, expected_secret)
 
    @patch('boto3.session.Session.client')
    def test_get_secret_invalid_secret(self, mock_client):
        """
        This method is used to test negative scenrios 
        for get the client object from Boto3 library 
        to get connect AWS secret manager
        """
        secret_name = "invalid-secret"
        mock_client.return_value.get_secret_value.side_effect = CustomError(
            {'Error': {'code': 'NoCredentialProviders',
                       'Message': 'No Credentials providers'}})
        with self.assertRaises(CustomError):
            get_secret(secret_name)
    
    @patch('psycopg2.connect')
    def test_connect_to_postgress_success(self, mock_psycopg2_connect):
        """
        This method is used to test postive scenrios
        for get the connection object from psycopy2 
        library to get connect 
        """
        credentials = {
            'host': "localhost",
            'port': 5432,
            'username': 'test_user',
            'password': 'test_passsword'
        }
        mock_conn = MagicMock(name='psycopg2.connect.return_value')
        mock_psycopg2_connect.return_value = mock_conn
        actual_connection = connect_to_postgres(credentials)
        self.assertEqual(actual_connection, mock_conn)
        
    @patch('psycopg2.connect')
    def test_connect_to_postgress_failure(self, mock_psycopg2_connect):
        """
        This method is used to test negative scenrios 
        for get the connection object from psycopy2 
        library to get connect 
        """
        credentials = {
            'host': "localhost",
            'port': 5432,
            'username': 'test_user',
            'password': 'test_passsword'
        }
        mock_conn = MagicMock(name='psycopg2.connect.return_value')
        mock_psycopg2_connect.return_value = mock_conn
        mock_psycopg2_connect.side_effect = Exception(
            "unable to connect to database")
        with self.assertRaises(Exception):
            connect_to_postgres(credentials)

if __name__ == '__main__':
    unittest.main()
