class Vehicle:
    def start(self):
        print("Vehicle start")
class Car(Vehicle):
    def drive(self):
        print("car is driving")
class ElectricVehicle(Car):
    def charge(self):
        print("electric car charging")

obj=ElectricVehicle()
obj.drive()
obj.start()                        