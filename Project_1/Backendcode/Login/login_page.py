import psycopg2
from psycopg2 import Error
from Backendcode.awsUtil.rds_connection import connect_to_postgres, get_secret
from Backendcode.dataBase.queries import FETCH_USER_CREDENTIALS

# secret_name = nam_aws_SM  #replace with you correct name
# secret_credentials = get_secret(secret_name)

def fetch_user_credentials(username):
    # secret_credentials are hardcoded here since , I have a plan of keeping the secret_credentials in 
    # AWS secrets manager which is not possible to use while all the setup is in local, So we are hard 
    # coding them directly in code, Usually we use get_secret function to fetch them from SM
    secret_credentials = {'password': 'Jyothi@143',
                   'username': 'REDDY',
                   'host': "localhost",
                   'port': "5432",
                   'database': "IONE"}
    connection = connect_to_postgres(secret_credentials)
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT username, password, active FROM users WHERE username = '{username}'"
            cursor.execute(query)
            user_data = cursor.fetchone()
            cursor.close()
            connection.close()
            return user_data
        except (Exception, Error) as error:
            print("Error fetching user credentials:", error)
            return None
    else:
        return None

def check_login(username, password):
    user_data = fetch_user_credentials(username)
    if user_data:
        saved_username, saved_password, active = user_data
        if active:
            if saved_password == password:
                print("Login successful!")
                return True
            else:
                print("Incorrect password!")
                return False
        else:
            print("User account is inactive!")
            return False
    else:
        print("User not found!")
        return False

# Example usage:
# Replace 'your_username' etc. with actual database credentials
# Replace 'users' with the actual table name
# Adjust the SQL query and comparison logic as per your database schema and requirements
# call check_login() function with username and password to check login

# Example usage:
# username = 'example_user'
# password = 'example_password'
# check_login(username, password)
