from abc import ABC,abstractmethod
class Payment(ABC):   #parent abstract class - define abstract method
    @abstractmethod
    def pay(self,amnt):
        pass


class Creditcard(Payment):   #child class-define how method works
    def pay(self,amnt):
        print("paid",amnt, "using credit card")
class UPI(Payment):
    def pay(self,amnt):
        print("paid",amnt,"using UPI")

P1=Creditcard()
P2=UPI()
P1.pay(1000)
P2.pay(2000)