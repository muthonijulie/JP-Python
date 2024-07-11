#raising exceptions
#defining exception class
class InvalidAgeError(Exception):
   #pass
   def __init__(self,message):
      self.message=message
def check_age(age):
    if age<0:
        raise InvalidAgeError("Age cannot be negative")#ValueError("Age cannot be negative")
    return age
try:
 user_input=int(input("Enter your age:"))
 print(check_age(user_input))
except InvalidAgeError as e:#ValueError as e:
 print(e)
 #print("Age cannot be negative")
 print("Code is running")