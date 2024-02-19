import psycopg2
import re
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from psycopg2 import Error
from Backendcode.awsUtil.rds_connection import connect_to_postgres, get_secret
from Backendcode.dataBase.queries import INSERT_USER

secret_credentials = psycopg2.connect(
    user="REDDY",
    password="Jyothi@143",
    host="localhost",
    port="5432",
    database="IONE"
)

def is_valid_email(email):
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.match(pattern, email) is not None

def generate_otp():
    # Generate a 6-digit OTP
    return ''.join(random.choices('0123456789', k=6))

def send_otp(email, otp):
    sender_email = "jyothireddy.01108@gmail.com"  # Replace with your email address
    receiver_email = email
    password = "Jyothi@143"  # Replace with your email password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Verification OTP"

    body = f"Your OTP for signup is: {otp}"
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)

def signup(username, email, password):
    if not is_valid_email(email):
        print("Invalid email format")
        return False

    connection = connect_to_postgres(secret_credentials)
    if connection:
        try:
            otp = generate_otp()
            send_otp(email, otp)

            cursor = connection.cursor()
            cursor.execute(INSERT_USER, (username, email, password, False, otp))
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except (Exception, Error) as error:
            print("Error signing up:", error)
            return False
    else:
        return False


# # signup_module.py
# import re
# import psycopg2
# from psycopg2 import Error
# from Backendcode.awsUtil.rds_connection import connect_to_postgres, get_secret
# from Backendcode.dataBase.queries import INSERT_USER

# # secret_name = your_db_name #replace with your database name
# # secret_credentials = get_secret(secret_name)
# secret_credentials = {'password': 'Jyothi@143',
#                    'username': 'REDDY',
#                    'host': "localhost",
#                    'port': "5432",
#                    'database': "IONE"}


# def is_valid_email(email):
#     # Regular expression pattern for a simple email validation
#     pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
#     return re.match(pattern, email) is not None

# def is_valid_password(password):
#     # Check if password meets criteria: at least 8 characters, 1 uppercase letter, 1 symbol
#     return len(password) >= 8 and any(c.isupper() for c in password) and any(not c.isalnum() for c in password)


# def signup(username, email, password):
#     if not is_valid_email(email):
#         print("Invalid email format")
#         return False
    
#     if not is_valid_password(password):
#         print("Invalid password format. Password should be at least 8 characters long, contain at least one uppercase letter, and at least one symbol.")
#         return False
#     # secret_credentials = {'password': 'Jyothi@143',
#     #                'username': 'REDDY',
#     #                'host': "localhost",
#     #                'port': "5432",
#     #                'database': "IONE"}
#     connection = connect_to_postgres(secret_credentials)
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute(INSERT_USER, (username, email, password, True))
#             connection.commit()
#             cursor.close()
#             connection.close()
#             return True
#         except (Exception, Error) as error:
#             print("Error signing up:", error)
#             return False
#     else:
#         return False



