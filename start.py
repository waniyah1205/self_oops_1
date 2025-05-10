class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"The {self.brand} car has started.")

# Create an instance of Car
car = Car(brand="Toyota")

# Accessing public variable and method from outside the class
print(car.brand)  # Output: Toyota
car.start()  # Output: The Toyota car has started.
