try:
    a=int(input("enter first value"))
    b=int(input("enter second value"))
    result=a/b;
    print(result)
except ZeroDivisionError:
    print("Zero division error")  
else:
    print("division by 0")           #no exception
finally:
    print("always run")        #file operation,resource relese,clean up operation,close files,proper resource management