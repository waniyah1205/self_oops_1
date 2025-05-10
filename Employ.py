class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

# Create an instance of Employee
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing variables
print(emp.name)        # Public: Works fine
print(emp._salary)     # Protected: Works fine, but conventionally should not be accessed directly
# print(emp.__ssn)     # Private: AttributeError because __ssn is name-mangled
