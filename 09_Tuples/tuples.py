
#A tuple is similar to a list, but it is immutable, which means that you cannot modify the values 
# in a tuple once it has been created In Python, you can create a tuple by enclosing a series of 
# values in parentheses and separating them with commas:


x = (1, 2, 3)
y = ("a", "b", "c")
z = (1, "a", 3.14)

#You can access the values in a tuple using indices (the position of the value in the tuple, starting from 0):
x = (1, 2, 3)
print(x[0])  # prints 1
print(x[1])  # prints 2
print(x[2])  # prints 3

#You can use slicing to access a range of values in a tuple:
x = (1, 2, 3, 4, 5)
print(x[1:3])  # prints (2, 3) (values at indices 1 and 2)
print(x[:3])  # prints (1, 2, 3) (values at indices 0, 1, and 2)
print(x[2:])  # prints (3, 4, 5) (values at indices 2, 3, and 4)

#You can use the len() function to find the length of a tuple:
x = (1, 2, 3)
len(x)  # returns 3
#Unlike lists, you cannot modify the values in a tuple once it has been created. However, you can create a new tuple by concatenating two tuples using the + operator:


x = (1, 2, 3)
y = (4, 5, 6)
z = x + y  # z is (1, 2, 3, 4, 5, 6)
#Tuples are useful when you need to store a set of values that you do not want to modify. They are also used as keys in dictionaries, since they are immutable.