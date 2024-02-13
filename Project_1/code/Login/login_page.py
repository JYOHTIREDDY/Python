import psycopg2
from psycopg2 import Error
from code.awsUtil.rds_connection import connect_to_postgres, get_secret
from code.dataBase.queries import FETCH_USER_CREDENTIALS

# secret_name = your_db_name #replace with your database name
# secret_credentials = get_secret(secret_name)
secret_credentials = psycopg2.connect(
        user="IONE",
        password="Jyothi@143",
        host="localhost",
        port="5432",
        database="IONE"
    )

def fetch_user_credentials(username):
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
