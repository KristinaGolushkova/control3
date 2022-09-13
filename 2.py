class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare_two(self):
        if self.name == "Bus":
            return self.capacity * 100 * 1.1
        else:
            return self.capacity * 100


School_bus = Bus("Bus", 12, 50)
print("Total Bus fare is:", School_bus.fare_two())
