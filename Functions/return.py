#return statement
#return single value
def sum(a,b):
    #print(f"Sum is {a+b}")
    return(a+b)
print(sum(4,8))

#return multiple value
def arithmetic_operations(a, b):

       return a + b, a - b, a * b, a / b

add, subtract, multiply, divide = arithmetic_operations(10, 2)

print(add, subtract, multiply, divide)  # Output: 12 8 20 5.0

#return none
def greet(name):

       print(f"Hello, {name}!")

result = greet("Alice")

print(result)  # Output: Hello, Alice!

                  


