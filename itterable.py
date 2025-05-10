class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Create an instance of Countdown
countdown = Countdown(5)

# Iterate through the countdown
for num in countdown:
    print(num)
