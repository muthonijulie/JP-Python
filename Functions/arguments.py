#default parameter
def greet(name):

       print(f"Hello, {name}!")

#greet()  # Output: Hello, Dan!
name=input("Enter your name:")
greet(name)
# greet("Mary")  # Output: Hello, Mary!

#keyword arguments
def greet(name,message):

       print(f"{message}, {name}!")

#greet()  # Output: Hello, Dan!
name=input("Enter your name:")
greet(name=name,message="Hello")
# greet("Mary")  # Output: Hello, Mary!

#positonal argument
def add(a, b):

       return a + b

result = add(5, 3)

print(result)  # Output: 8

#Variable-Length Arguments:
def add_all(a,b,c):

       return a+b+c

print(add_all(1, 2, 3)) 

#args
def add_all(*args):

       return sum(args)

print(add_all(1, 2, 3,8,9,7)) 

#kwargs
def print_details(**kwargs):

       for key, value in kwargs.items():

           print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")



