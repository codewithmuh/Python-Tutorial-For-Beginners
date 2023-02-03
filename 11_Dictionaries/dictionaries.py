#A dictionary is a collection of key-value pairs. In Python, you can create a dictionary by
# enclosing a series of key-value pairs in curly braces and separating them with commas:


x = {'a': 1, 'b': 2, 'c': 3}
y = {'fruit': 'apple', 'animal': 'dog'}

#You can access the values in a dictionary using the keys:
x = {'a': 1, 'b': 2, 'c': 3}
print(x['a'])  # prints 1
print(x['b'])  # prints 2
print(x['c'])  # prints 3

#You can use the len() function to find the length of a dictionary (the number of key-value pairs):
x = {'a': 1, 'b': 2, 'c': 3}
len(x)  # returns 3

#You can use the in operator to check if a key is in a dictionary:
x = {'a': 1, 'b': 2, 'c': 3}
print('a' in x)  # prints True
print('d' in x)  # prints False


#You can use the get() method to retrieve the value for a given key:
x = {'a': 1, 'b': 2, 'c': 3}
print(x.get('a'))  # prints 1
print(x.get('d'))  # prints None

#You can use the update() method to add a new key-value pair to a dictionary:
x = {'a': 1, 'b': 2, 'c': 3}
x.update({'d': 4})  # x is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#You can use the pop() method to remove a key-value pair from a dictionary:
x = {'a': 1, 'b': 2, 'c': 3}
x.pop('b')  # x is now {'a': 1, 'c': 3}

#Dictionaries are useful when you need to store a collection of values that are related to each other,
# and you want to be able to access the values using keys.

# https://youtube.com/@codewithmuh