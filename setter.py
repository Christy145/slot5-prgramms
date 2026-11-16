class Bank:
    def __init__(self):
        self.__balance=5000
    def get_balance(self):          #getter method
        return self.__balance
    def set_balance(self,amount):   #setter method
        if amount>7000:
            self.__balance=amount


obj=Bank()
obj.set_balance(9000)
print(obj.get_balance())          
