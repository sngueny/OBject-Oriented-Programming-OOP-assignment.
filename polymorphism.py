class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Bicycle:
    def move(self):
        print("Riding 🚲")

# Creating objects of each class
car = Car()
plane = Plane()
bicycle = Bicycle()

# Calling move() for each object
vehicles = [car, plane, bicycle]
for vehicle in vehicles:
    vehicle.move()
