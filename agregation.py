class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        # Aggregation: Department has a reference to Employee objects
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"Employees in {self.name} Department:")
        for emp in self.employees:
            print(f"{emp.name}, {emp.position}")

# Create Employee objects
emp1 = Employee(name="Alice", position="Manager")
emp2 = Employee(name="Bob", position="Developer")

# Create a Department object
department = Department(name="IT")

# Add employees to the department
department.add_employee(emp1)
department.add_employee(emp2)

# List employees
department.list_employees()
