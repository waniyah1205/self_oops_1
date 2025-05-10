class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

# Create an object of D
d = D()
d.show()  # Output: Class B (MRO: D -> B -> C -> A)
