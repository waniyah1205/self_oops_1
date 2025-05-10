class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Create instances of Counter
obj1 = Counter()
obj2 = Counter()

# Display object count
Counter.display_count()
