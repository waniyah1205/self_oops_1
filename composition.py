class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        # Composition: Car has an Engine object
        self.engine = engine
    
    def drive(self):
        self.engine.start()  # Calling the Engine method from Car
        print("Car is driving.")

# Create an Engine object
engine = Engine()

# Create a Car object and pass the Engine object to it
car = Car(engine)

# Drive the car
car.drive()  # Output: Engine started. Car is driving.
