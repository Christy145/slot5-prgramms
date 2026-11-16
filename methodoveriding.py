class Vehicle:
    def speed(self):
        print("The speed is 100")
class Car(Vehicle):
    def drive(self):
         super().speed()
        print("car is driving")
class ElectricVehicle(Car):
    def charge(self):
        print("electric car charging")

obj=Car()
obj.speed() 



#issue-method overriding
#child class method override parent class method
#super()-solve this issue