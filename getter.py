class Bank:
    def __init__(self):
        self.__balance=5000
    def get_balance(self):          #getter method
        return self.__balance


obj=Bank()
print(obj.get_balance())    
            