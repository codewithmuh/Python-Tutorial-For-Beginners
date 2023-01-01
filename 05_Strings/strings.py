#what is string 

# A string is a data type used in programming, that is used to represent text rather
# than numbers. A string is a sequence of characters and can contain letters, numbers, symbols and even spaces.
# It must be enclosed in quotation marks for it to be recognized as a string.


x = "hello"
y = 'world'
#You can access the characters in a string using indices (the position of the character in the string, starting from 0):


x = "hello"
print(x[0])  # prints "h"
print(x[1])  # prints "e"
print(x[2])  # prints "l"
#You can use slicing to access a range of characters in a string:


x = "hello"
print(x[1:3])  # prints "el" (characters at indices 1 and 2)
print(x[:3])  # prints "hel" (characters at indices 0, 1, and 2)
print(x[2:])  # prints "llo" (characters at indices 2, 3, and 4)
#You can use the len() function to find the length of a string:


x = "hello"
len(x)  # returns 5
#You can also use the + operator to concatenate two strings:


x = "hello"
y = "world"
z = x + y  # z is "helloworld"
#There are many other operations and methods that you can use with strings in Python. It's a good idea t
# familiarize yourself with these so that you can use strings effectively in