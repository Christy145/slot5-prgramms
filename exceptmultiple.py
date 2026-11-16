try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divisible by 0")
except ValueError:
    print("please enter valid no")    
