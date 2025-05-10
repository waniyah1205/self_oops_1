class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Price is being deleted")
        del self._price

# Create an instance of Product
product = Product(100)
print(product.price)  # Output: 100

# Update the price using the setter
product.price = 150
print(product.price)  # Output: 150

# Delete the price
del product.price  # Output: Price is being deleted

