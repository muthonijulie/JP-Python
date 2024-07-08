#empty tuple
empty_tuple=()

#A tuple of integers
numbers = (1, 2, 3, 1, 5)
print(numbers[0])  
print(numbers[-1]) 
print(numbers[1:4])

#count
count = numbers.count(1)
print(count)
#index
index = numbers.index(1)
print(index) 

print(numbers)

#A tuple of strings
words = ("apple", "banana", "cherry")
print(words)

 #A tuple of mixed data types
mixed = (1, "apple", 3.14, True)
print(mixed[1:2])

 #A tuple of tuples (nested tuple)
nested = ((1, 2), (3, 4), (5, 6))
print(nested)

#packing
packed_tuple = 1, "apple", 3.14

print(packed_tuple)

#unpacking
num, fruit, pi = packed_tuple

print(num)    

print(fruit) 

print(pi)

#multiple values
def get_coordinates():

       return 10, 20

x, y = get_coordinates()

print(x, y)

#fixed data collection
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days_of_week )

#dictionary keys
locations = {

       (40.7128, -74.0060): "New York",

       (34.0522, -118.2437): "Los Angeles",

   }
print(locations)

#list to tuple
numbers_list = [1, 2, 3, 4, 5]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)

#tuple to list
numbers_tuple = (1, 2, 3, 4, 5)

numbers_list = list(numbers_tuple)

print(numbers_list)