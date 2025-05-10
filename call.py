class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Create an instance of Multiplier
multiplier = Multiplier(3)

# Test callable
print(callable(multiplier))  # Output: True

# Calling the object like a function
print(multiplier(5))  # Output: 15
