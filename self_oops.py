# 01_student_self.py

class Student:
    def __init__(self, name, marks):
        self.name = name        # instance variable for student's name
        self.marks = marks      # instance variable for student's marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


if __name__ == "__main__":
    # Creating student objects
    student1 = Student("Alia", 85)
    student2 = Student("Mohsin", 92)

    # Display their details
    student1.display()
    print("-----")
    student2.display()
