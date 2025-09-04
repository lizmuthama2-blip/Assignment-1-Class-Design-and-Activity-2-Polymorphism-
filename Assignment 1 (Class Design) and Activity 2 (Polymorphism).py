class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__status = "Off"    Private attribute (encapsulation)
    def power_on(self):
        self.__status = "On"
        return f"{self.brand} {self.model} is now ON "
    def power_off(self):
        self.__status = "Off"
        return f"{self.brand} {self.model} is now OFF "
    def get_status(self):
        return f"Current status: {self.__status}"
class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand, model)  # Inherit brand & model from Device
        self.storage = storage
    def call(self, number):
        return f"Calling {number}..."
    def take_photo(self):
        return f"Photo taken with {self.brand} {self.model} "
Activity 2: Polymorphism
class Vehicle:
    def move(self):
        return "This vehicle moves somehow "
class Car(Vehicle):
    def move(self):
        return "Driving "
class Plane(Vehicle):
    def move(self):
        return "Flying "
class Boat(Vehicle):
    def move(self):
        return "Sailing "
print("=== Assignment 1: Smartphone Class ===")
phone1 = Smartphone("Samsung", "Galaxy S22", "128GB")
print(phone1.power_on())
print(phone1.call("0715213277"))
print(phone1.take_photo())
print(phone1.get_status())
print(phone1.power_off())
print("\n=== Activity 2: Polymorphism Challenge ===")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())
