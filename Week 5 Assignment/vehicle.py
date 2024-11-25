class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Generic vehicle movement")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on road 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in sky ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on water 🚢")

def demonstrate_movement(vehicle):
    vehicle.move()

tesla = Car("Tesla Model S")
boeing = Plane("Boeing 747")
yacht = Boat("Luxury Yacht")


vehicles = [tesla, boeing, yacht]
for vehicle in vehicles:
    demonstrate_movement(vehicle)