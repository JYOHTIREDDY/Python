from flask import Flask, request, jsonify
import psycopg2
import json
import boto3
from ..code.awsUtil.rds_connection import get_secret, connect_to_postgres

app = Flask(__name__)

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

def get_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    try:
        response = client.get_secret_value(SecretId=secret_name)
    except Exception as err:
        raise err
    else:
        if 'SecretString' in response:
            secret = json.loads(response['SecretString'])
            return secret
        else:
            raise ValueError("SecretString not found in the response from AWS Secrets Manager.")

# def connect_to_postgres(credentials):
#     try:
#         conn = psycopg2.connect(
#             host=credentials['host'],
#             port=credentials['port'],
#             user=credentials['username'],
#             password=credentials['password'],
#             database=credentials['database']
#         )
#         return conn
#     except Exception as err:
#         raise err

def fetch_user_credentials(username):
    credentials = {'password': 'Jyothi@143',
                   'username': 'REDDY',
                   'host': "localhost",
                   'port': "5432",
                   'database': "IONE"}
    connection = connect_to_postgres(credentials)
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT username, password, active FROM users WHERE username = '{username}'"
            cursor.execute(query)
            user_data = cursor.fetchone()
            cursor.close()
            connection.close()
            return user_data
        except Exception as error:
            print("Error fetching user credentials:", error)
            return None
    else:
        return None

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Authenticate user
    if check_login(username, password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask

# app = Flask(__name__)





# @app.route("/members")
# def members():
#     return{"members" : ["member1", "member2"]}

# if __name__ == "__main__":
#     app.run(debug = True)