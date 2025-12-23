class BMW:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    
    def FuelType(self):
        return f"BMW Fuel Type: {self.fuel_type}"
    
    def MaxSpeed(self):
        return f"BMW Max Speed: {self.max_speed} km/h"


class Ferrari:
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    
    def FuelType(self):
        return f"Ferrari Fuel Type: {self.fuel_type}"
    
    def MaxSpeed(self):
        return f"Ferrari Max Speed: {self.max_speed} km/h"


# Polymorphism in action
cars = [BMW("Diesel", 240), Ferrari("Petrol", 340)]

for car in cars:
    print(car.FuelType())
    print(car.MaxSpeed())
    print()