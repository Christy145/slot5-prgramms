from abc import ABC,abstractmethod
class Vehicle(ABC):   #parent abstract class - define abstract method
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):   #child class-define how method works
    def start(self):
        print("car starting...")
c=Car()  
c.start()          