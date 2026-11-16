class MyException(Exception):
    pass


age=int(input("enter age:"))
try:
    if age<18:
        print("Not eligible")
        raise MyException ("invalid")
    else:
        print("Eligible")
except MyException as e:
    print(e)            