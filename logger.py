class Logger:
    def __init__(self):
        print("Object created.")
    
    def __del__(self):
        print("Object destroyed.")

# Create and destroy an instance of Logger
logger = Logger()
del logger  # Output: Object created. Object destroyed.
