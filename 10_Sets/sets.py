#A set is an unordered collection of unique values. In Python, you can create a set by enclosing a series
# of values in curly braces and separating them with commas:

x = {1, 2, 3}
y = {"a", "b", "c"}
z = {1, "a", 3.14}


#Sets do not have indices, so you cannot access the values in a set using indices. However, you can use the len()
# function to find the length of a set:
x = {1, 2, 3}
len(x)  # returns 3

#You can use the in operator to check if a value is in a set:
x = {1, 2, 3}
print(1 in x)  # prints True
print(4 in x)  # prints False

#You can use the add() method to add a value to a set:
x = {1, 2, 3}
x.add(4)  # x is now {1, 2, 3, 4}


#You can use the remove() method to remove a value from a set:
x = {1, 2, 3}
x.remove(2)  # x is now {1, 3}

#You can use the union() method to create a new set that contains all the values from two sets:
x = {1, 2, 3}
y = {3, 4, 5}
z = x.union(y)  # z is {1, 2, 3, 4, 5}

#You can use the intersection() method to create a new set that contains only the values that are common to both sets:
x = {1, 2, 3}
y = {3, 4, 5}
z = x.intersection(y)  # z is {3}
#Sets are useful when you need to store a collection of unique values and perform set operations, such as union and
# intersection.