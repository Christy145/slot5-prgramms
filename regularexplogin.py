import re
print("---Registration---")
def registration():
    phone=input("enter the number")
    email=input("enter the email")
    password=input("enter the password")
    if not re.fullmatch(r"[0-9]{10}$",phone):
        print("valid phone number")
    elif not re.fullmatch(r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}",email):
        print("valid email")
    elif not  re.fullmatch(r"^[a-z]+$",password):
         print("valid password")  
    else:
         print("registration successfull")
registration()         


print("--Login--")
def login():
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
        print("login successful") 
login()              


 




       
                  

