import re

num=input("enter the number")
pattern=r"^[0-9]{10}$"
if re.fullmatch(pattern,num):
    print(" valid phone number")
else:
    print("invalid phone number")       