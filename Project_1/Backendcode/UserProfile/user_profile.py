import psycopg2
from psycopg2 import Error
from Backendcode.awsUtil.rds_connection import connect_to_postgres, get_secret
from Backendcode.dataBase.queries import FETCH_USER_PROFILE, UPDATE_USER_PROFILE


# secret_name = your_db_name #replace with your database name
# secret_credentials = get_secret(secret_name)
secret_credentials = psycopg2.connect(
        user="IONE",
        password="Jyothi@143",
        host="localhost",
        port="5432",
        database="IONE"
    )
def fetch_user_profile(username):
    connection = connect_to_postgres(secret_credentials)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(FETCH_USER_PROFILE, (username,))
            user_profile = cursor.fetchone()
            cursor.close()
            connection.close()
            return user_profile
        except (Exception, Error) as error:
            print("Error fetching user profile:", error)
            return None
    else:
        return None

def update_user_profile(username, new_profile_data):
    connection = connect_to_postgres(secret_credentials)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(UPDATE_USER_PROFILE, (new_profile_data, username))
            connection.commit()
            cursor.close()
            connection.close()
            print("User profile updated successfully!")
            return True
        except (Exception, Error) as error:
            print("Error updating user profile:", error)
            return False
    else:
        return False

# Example usage:
# Replace 'your_username' etc. with actual database credentials
# Replace 'users' with the actual table name
# Adjust the SQL queries as per your database schema and requirements

# To fetch user profile after login
# username = 'example_user'
# user_profile = fetch_user_profile(username)
# print("User Profile:", user_profile)

# To update user profile
# new_profile_data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'}
# update_user_profile(username, new_profile_data)
