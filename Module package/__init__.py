#general
from myPackage import module1, module2

print(module1.func1())  # Output: Function 1 from module 1
print(module2.func2())  # Output: Function 2 from module 2

#Import specific functions
from myPackage.module1 import func11
from myPackage.module2 import func2

print(func11())  # Output: Function 1 from module 1
print(func2())  # Output: Function 2 from module 2