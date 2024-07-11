def operations():
 try:
    result = 10 / 0
 except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

    #Multiple Except Blocks
 try:
    value = int("abc")
 except ValueError:
    print("Error: Invalid literal for integer.")
   
 try:
    result = "hello" + 5
 except TypeError:
    print("Error: Cannot concatenate string and integer.")

    #else clause
    
 try:
    result = 10 / 2
 except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
 else:
    print(f"Result is {result}")

    #finally

 try:
    file = open("read.txt", "r")
    content = file.read()
 except FileNotFoundError:
    print("Error: File not found.")
 finally:
    if file:
        file.close()
    print("File closed.")
operations()