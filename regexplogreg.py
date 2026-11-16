import re

def registration():
    phone=input("enter mobile number")
    email=input("enter email")
    password=input("enter password")

    if not re.fullmatch(r"[0-9]{10}$",phone):
    print("valid phone number")
    elif not re.fullmatch(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}",email):
    print("valid email")
    elif not  re.fullmatch(r"^[a-z]+$",password):
    print("valid password")  
    else:
    print("registration successfull")