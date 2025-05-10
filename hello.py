def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
person = Person("John")
print(person.greet())  # Output: Hello from Decorator!

