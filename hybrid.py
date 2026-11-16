#class A:
    #pass
#class B(A):
    #pass
#class C(A):
    #pass
#class D(B,C):
    #pass


class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle")
class Car(Vehicle):
    def car_info(self):
        print("This is car ")
class Bike(Vehicle):
    def bike_info(self):
        print("This is Bike")
class ElectricVehicle(Car,Bike):
    def en_info(self):
        print("This is an electric vehicle")
ev=ElectricVehicle()
ev.vehicle_info()
ev.car_info()  
ev.bike_info()
ev.en_info()                      

