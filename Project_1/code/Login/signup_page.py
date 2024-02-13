# signup_module.py

import psycopg2
from psycopg2 import Error
from code.awsUtil.rds_connection import connect_to_postgres, get_secret
from code.dataBase.queries import INSERT_USER

# secret_name = your_db_name #replace with your database name
# secret_credentials = get_secret(secret_name)
secret_credentials = psycopg2.connect(
        user="REDDY",
        password="Jyothi@143",
        host="localhost",
        port="5432",
        database="IONE"
    )


def is_valid_email(email):
    # Regular expression pattern for a simple email validation
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    # Check if password meets criteria: at least 8 characters, 1 uppercase letter, 1 symbol
    return len(password) >= 8 and any(c.isupper() for c in password) and any(not c.isalnum() for c in password)


def signup(username, email, password):
    if not is_valid_email(email):
        print("Invalid email format")
        return False
    
    if not is_valid_password(password):
        print("Invalid password format. Password should be at least 8 characters long, contain at least one uppercase letter, and at least one symbol.")
        return False
    
    connection = connect_to_postgres(secret_credentials)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(INSERT_USER, (username, email, password, True))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except (Exception, Error) as error:
            print("Error signing up:", error)
            return False
    else:
        return False



