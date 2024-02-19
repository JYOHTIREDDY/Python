import sys
sys.path.append('/path/to/code')


from Backendcode.Login.signup_page import *
from Login.login_page import *
from UserProfile.user_profile import *



def practical_run():
    user_id        =     'JYOTHI0110',
    username       =     'JYOTHI0110',
    email          =     'myemail@gmail.com',
    password       =     '1234567890',
    first_name     =     'jyothi reddy',
    last_name      =     'dondapati',
    active         =     True
    signup(username, email, password)
    if signup :
        print("Signup successfull\n Trying login")
        if check_login(username, password):
            print("login successfull\n Trying login")
        else:
            print("login Failed")   
    else:
        print("Signup Failed")
    return "Successfull" 

practical_run()