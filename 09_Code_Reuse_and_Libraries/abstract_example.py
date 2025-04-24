from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle started")
        
def create_vehicle(vehicle_type):
    if vehicle_type == "car":
        return Car()
    elif vehicle_type == "motorcycle":
        return Motorcycle()
    else:
        raise ValueError("Unknown vehicle type")

car = create_vehicle("car")
car.start() 

motorcycle = create_vehicle("motorcycle")
motorcycle.start()