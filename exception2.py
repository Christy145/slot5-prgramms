class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount >self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.balance -= amount
        print("withdraw success")
try:
    obj=BankAccount(5000)
    obj.withdraw(9000)
except InsufficientBalanceError as  e:
    print("Error:",e)   
