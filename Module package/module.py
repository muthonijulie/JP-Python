def greet(name):
    return f"Hello, {name}!"


pi=3.1425
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return pi *(self.radius**2)
    
import math

print(math.sqrt(16))  # Output: 4.0
print(math.pi) 

import datetime
now = datetime.datetime.now()
print(now)  # Output: current date and time
today = datetime.date.today()
print(today) 


import os

current_dir = os.getcwd()
print(current_dir)  # Output: current working directory
os.mkdir('new_directory')  # Create a new directory

