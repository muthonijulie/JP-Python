#empty list
empty_list=[]
#list of numbers
num=[2,3,5,7,9]
print(num[2])
#Negative indexing starts from the end of the list.
print(num[-1])
print(num[2:4])
#since lists are mutable, i have changed the value at index 2 to 54
num[2]=54
#adds item at the end of the list
num.append(32)
#add item at a specified index
num.insert(3,65)
#adds mulitple items to the end of the list
num.extend([3,6])
#removes first occurence of an item
num.remove(3)
#Removes and returns the item at the specified index
last_item=num.pop()
print(last_item)
#removes all items from the list
#num.clear()
#sorts list in an ascending order
num.sort()
#reverse the order of the list
num.reverse()
#Returns the index of the first occurrence of an item.
index=num.index(3)
print(index)
#Returns the number of occurrences of an item.
count=num.count(9)
print(count)
new_num=num.copy()
print(new_num)
print(num)

#A list of strings
words = ["apple", "banana", "cherry"]
print(words[1:3])#output banana,cherry

#A list of mixed data types
mixed = [1, "apple", 3.14, True]
print(mixed[0:3])

#A list of lists (nested list)
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[2])
#list comprehensions
#square
squares = [x**2 for x in range(10)]

print(squares) 

#even
evens = [x for x in range(20) if x % 2 == 0]

print(evens)

#list with functions
def square_list(numbers):

    return [x**2 for x in numbers]

numbers = [1, 2, 3, 4,5,6,7]

squared_numbers = square_list(numbers)

print(squared_numbers)