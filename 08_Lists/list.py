

#A list is an ordered collection of values that can be of any data type. In Python, you can create a list by
# enclosing a series of values in square brackets and separating them with commas:


x = [1, 2, 3]
y = ["a", "b", "c"]
z = [1, "a", 3.14]

#You can access the values in a list using indices (the position of the value in the list, starting from 0):

x = [1, 2, 3]
print(x[0])  # prints 1
print(x[1])  # prints 2
print(x[2])  # prints 3


#You can use slicing to access a range of values in a list:
x = [1, 2, 3, 4, 5]
print(x[1:3])  # prints [2, 3] (values at indices 1 and 2)
print(x[:3])  # prints [1, 2, 3] (values at indices 0, 1, and 2)
print(x[2:])  # prints [3, 4, 5] (values at indices 2, 3, and 4)
#You can use the len() function to find the length of a list:

x = [1, 2, 3]
len(x)  # returns 3
#You can use the + operator to concatenate two lists:


# https://youtube.com/@codewithmuh