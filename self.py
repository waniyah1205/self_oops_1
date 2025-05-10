class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create an instance of Student
student = Student(name="John Doe", marks=85)
student.display()
