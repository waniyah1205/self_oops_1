class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the constructor of Person
        self.subject = subject

# Create an instance of Teacher
teacher = Teacher("Alice", "Mathematics")
print(teacher.name)    # Output: Alice
print(teacher.subject) # Output: Mathematics
