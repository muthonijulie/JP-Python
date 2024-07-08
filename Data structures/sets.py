# # An empty set
# empty_set = set()
# print(empty_set)

# # A set of integers
# #set does not allow repetition
# numbers = {34,32,1,5,6,1}
# print(numbers)

# # A set of strings
# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# # A set with mixed data types
# mixed = {1, "apple", 3.14, True}
# print(mixed)

# # Creating a set from a list
# numbers_list = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers_list)
# print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# #accessing set items
# fruits = {"apple", "banana", "cherry"}
# for fruit in fruits:
#     print(fruit)

# #Add Items

# fruits = {"apple", "banana"}
# fruits.add("cherry")
# print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# #Update Set with Multiple Items:

# fruits.update(["orange", "mango"])
# print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange', 'mango'}


# #Removes the specified item. Raises a `KeyError` if the item is not found.
# fruits.remove("banana")
# print(fruits)  # Output: {'apple', 'cherry', 'orange', 'mango'}

# #Removes the specified item. Does not raise an error if the item is not found.

# fruits.discard("banana")
# print(fruits)  # Output: {'apple', 'cherry', 'orange', 'mango'}

# #Removes and returns an arbitrary item. Raises a `KeyError` if the set is empty.

# item = fruits.pop()
# print(item)
# print(fruits)

# #Removes all items from the set.

# fruits.clear()
# print(fruits)  # Output: set()

#set operations
a = {1, 2, 3}
b = {3, 4, 5}
# union= a | b
# print(union)  # Output: {1, 2, 3, 4, 5}

# intersection_set = a & b
# print(intersection_set) 

# difference_set = a - b
# print(difference_set)  # Output: {1, 2}

# sym_diff_set = a ^ b
# print(sym_diff_set)  # Output: {1, 2, 4, 5}

# #example of set methods
# a.add(6)
# print(a)  # Output: {1, 2, 3, 6}

#frozen set
fs = frozenset([1, 2, 3, 4, 5])

print(fs)  # Output: frozenset({1, 2, 3, 4, 5})