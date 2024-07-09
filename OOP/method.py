class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Instantiate the Circle class
my_circle = Circle(5)

# Calling methods
print(my_circle.area())      
print(my_circle.perimeter())