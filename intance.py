class Dog:
    def __init__(self, name, breed):
        # Initializing instance variables
        self.name = name
        self.breed = breed
    
    def bark(self):
        # Instance method to print the dog's name and a bark message
        print(f"{self.name} says woof!")

# Create an instance of Dog
dog = Dog(name="Buddy", breed="Golden Retriever")

# Call the instance method
dog.bark()  # Output: Buddy says woof!

