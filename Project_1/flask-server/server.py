from flask import Flask, request, jsonify
import json
import os
import sys
import random
import string
import smtplib
from email.mime.text import MIMEText
dir_main = os.path.dirname(os.path.dirname((__file__)))
sys.path.insert(0, dir_main)
# Import necessary functions from your modules
from Backendcode.awsUtil.rds_connection import get_secret, connect_to_postgres
from Backendcode.Login.login_page import fetch_user_credentials, check_login
from Backendcode.Login.signup_page import signup

app = Flask(__name__)

# Generate OTP
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

# Send OTP to user's email
# Send OTP to user's email
def send_otp_email(email, otp):
    try:
        smtp_server = 'smtp.gmail.com'  # Replace 'your_smtp_server' with the SMTP server address
        smtp_port = 587  # Replace with the appropriate port number if different
        sender_email = 'jyothireddy.01108@gmail.com"'  # Replace with your sender email address
        sender_password = 'Jyothi@143'  # Replace with your sender email password
        
        message = MIMEText(f'Your OTP is: {otp}')
        message['Subject'] = 'OTP Verification'
        message['From'] = sender_email
        message['To'] = email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [email], message.as_string())
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    action = data.get('action')
    email = data.get('email')
    otp = data.get('otp')

    if action == 'login':
        if check_login(username, password):
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    elif action == 'signup':
        if not otp:
            # Generate OTP and send it to user's email
            otp = generate_otp()
            if send_otp_email(email, otp):
                return jsonify({'message': 'OTP sent to your email. Please check your inbox.', 'otp': otp})
            else:
                return jsonify({'message': 'Failed to send OTP'}), 500
        else:
            # Verify OTP
            if signup(username, email, password, otp):
                return jsonify({'message': 'Signup successful'})
            else:
                return jsonify({'message': 'Invalid OTP'}), 401
    else:
        return jsonify({'message': 'Invalid action'})

@app.route("/signup/request-otp", methods=['POST'])
def request_otp():
    data = request.get_json()
    email = data.get('email')
    otp = generate_otp()
    if send_otp_email(email, otp):
        return jsonify({'message': 'OTP sent to your email. Please check your inbox.', 'otp': otp})
    else:
        return jsonify({'message': 'Failed to send OTP'}), 500

if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask, request, jsonify
# import json
# import os
# import sys
# dir_main = os.path.dirname(os.path.dirname((__file__)))
# sys.path.insert(0, dir_main)
# from Backendcode.awsUtil.rds_connection import get_secret, connect_to_postgres
# from Backendcode.Login.login_page import fetch_user_credentials, check_login
# from Backendcode.Login.signup_page import signup

# app = Flask(__name__)

# @app.route("/login", methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     action = data.get('action')
#     email = data.get('email')

#     # Authenticate user
#     if action == 'login':
#         if check_login(username, password):
#             return jsonify({'message': 'Login successful'})
#         else:
#             return jsonify({'message': 'Invalid username or password'}), 401
#     elif action == 'signup':
#         signup(username, email, password)
#         return jsonify({'message': 'Signup successful'})
#     else:
#         return jsonify({'message': 'Invalid action'})

# if __name__ == "__main__":
#     app.run(debug=True)
