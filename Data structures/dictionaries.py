# An empty dictionary
empty_dict = {}
print(empty_dict)

# A dictionary with integer keys
numbers = {1: 'one', 2: 'two', 3: 'three'}
print(numbers)

# A dictionary with string keys
fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruits)

# A dictionary with mixed data types
mixed = {"name": "Alice", "age": 30, "is_student": False}
print(mixed)

# A dictionary using the dict() constructor
person = dict(name="Alice", age=30, is_student=False)
print(person)

#accessing items
fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruits["cherry"])
print(fruits.get("banana"))  # Output: yellow
print(fruits.get("orange", "not found"))  # Output: not found

#changing items
fruits["apple"] = "green"
print(fruits)

#adding items
fruits["orange"] = "orange"
print(fruits)

#remove
color = fruits.pop("banana")
print(color)  # Output: yellow
print(fruits)

#removes the last inserted item
item = fruits.popitem()
print(item)  # Output: ('orange', 'orange')
print(fruits)

#remove item with specified key or deletes the entire dictionay
del fruits["cherry"]
print(fruits)

#clear all items from dictionary
fruits.clear()
print(fruits) # Output: {}

 #Returns a view object containing the dictionary’s keys.

fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
keys = fruits.keys()
print(keys)  # Output: dict_keys(['apple', 'banana', 'cherry'])

#Returns a view object containing the dictionary’s values.

values = fruits.values()
print(values)  # Output: dict_values(['red', 'yellow', 'red'])

#Returns a view object containing the dictionary’s key-value pairs.

items = fruits.items()
print(items)  # Output: dict_items([('apple', 'red'), ('banana', 'yellow'), ('cherry', 'red')])

#Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.

more_fruits = {"orange": "orange", "pear": "green"}
fruits.update(more_fruits)
print(fruits)  # Output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'orange': 'orange', 'pear': 'green'}

#Returns a shallow copy of the dictionary.

fruits_copy = fruits.copy()
print(fruits_copy)  # Output: {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'orange': 'orange', 'pear': 'green'}


#dictionary comprehensions
# Create a dictionary of squares
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Create a dictionary from two lists
keys = ["name", "age", "country"]
values = ["Alice", 25, "USA"]
info = {keys[i]: values[i] for i in range(len(keys))}
print(info)

#nested dictionary
people = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
}
print(people["person1"]["name"]) 