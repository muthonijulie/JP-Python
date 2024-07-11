# main.py
# Import the entire module
import module

print(module.greet("Liz"))
print(f"Pi value: {module.pi}")
circle = module.Circle(5)
print(f"Area of circle: {circle.area()}")


# Import specific attributes
from module import greet, pi, Circle

print(greet("Bob"))
print(f"Pi value: {pi}")
circle = Circle(7)
print(f"Area of circle: {circle.area()}")

# Import with an alias
import module as mm

print(mm.greet("Charlie"))
print(f"Pi value: {mm.pi}")
circle = mm.Circle(10)
print(f"Area of circle: {circle.area()}")
