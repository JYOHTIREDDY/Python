from flask import Flask, request, jsonify
import random
import string
import time

app = Flask(__name__)

# Dictionary to store OTPs and their creation timestamps
otp_store = {}

@app.route('/send_otp', methods=['POST'])
def send_otp():
    phone_number = request.json.get('phone_number')
    if phone_number:
        otp = generate_otp(phone_number)
        if otp:
            return jsonify({"message": "OTP sent successfully"}), 200
        else:
            return jsonify({"message": "Failed to send OTP"}), 500
    else:
        return jsonify({"message": "Phone number not provided"}), 400

def generate_otp(phone_number):
    # Generate a random 6-digit OTP (you can customize the length as needed)
    otp = ''.join(random.choice(string.digits) for _ in range(6))

    # Store OTP and its creation time
    otp_store[phone_number] = {'otp': otp, 'timestamp': time.time()}

    # Here you would typically send the OTP via SMS using Twilio or another service
    # For simplicity, we'll just return the OTP here
    return otp

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    phone_number = request.json.get('phone_number')
    user_entered_otp = request.json.get('otp')

    if phone_number and user_entered_otp:
        is_verified, message = verify_phone_number(phone_number, user_entered_otp)
        return jsonify({"message": message}), 200 if is_verified else 400
    else:
        return jsonify({"message": "Phone number or OTP not provided"}), 400

def verify_phone_number(phone_number, user_entered_otp):
    if otp_store.get(phone_number) and otp_store[phone_number]['otp'] == user_entered_otp:
        creation_time = otp_store[phone_number]['timestamp']
        current_time = time.time()
        if current_time - creation_time <= 180:  # 3 minutes (180 seconds) expiry
            return True, "Phone number verified successfully!"
        else:
            return False, "OTP has expired. Phone number verification failed."
    else:
        return False, "Incorrect OTP. Phone number verification failed."

if __name__ == '__main__':
    app.run(debug=True)




# from twilio.rest import Client

# # Twilio credentials
# TWILIO_ACCOUNT_SID = 'your_account_sid'
# TWILIO_AUTH_TOKEN = 'your_auth_token'
# TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# def send_otp(phone_number):
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#     try:
#         # Generate a random 6-digit OTP (you can customize the length as needed)
#         otp = ''.join(random.choice(string.digits) for _ in range(6))

#         # Send OTP via SMS
#         message = client.messages.create(
#             body=f"Your OTP is: {otp}",
#             from_=TWILIO_PHONE_NUMBER,
#             to=phone_number
#         )
#         return otp
#     except Exception as e:
#         print("Error sending OTP:", e)
#         return None

# def verify_phone_number(phone_number):
#     otp = send_otp(phone_number)
#     if otp:
#         # Here you would typically prompt the user to enter the OTP received
#         user_entered_otp = input("Please enter the OTP received: ")
#         if user_entered_otp == otp:
#             print("Phone number verified successfully!")
#             return True
#         else:
#             print("Incorrect OTP. Phone number verification failed.")
#             return False
#     else:
#         print("Failed to send OTP. Phone number verification failed.")
#         return False

# # Example usage:
# phone_number = '+1234567890'  # Replace with the phone number to verify
# verify_phone_number(phone_number)



##############
# as of now lets assume the we will update the DB without any phonenum validation
# but we will have something to show as a verified user when the user did verification
# for phone number (which can be a completly differetnt api call)

# If possible try to do phone number and email validation at once so that it can be one api call
# from front end to back end
##############