try:
    f=open("file.txt")
except:
    print("file not found")
finally:
    file.close()        