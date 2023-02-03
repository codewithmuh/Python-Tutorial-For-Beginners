

# Functions are blocks of reusable code in Python that can be called with specified inputs (arguments). Functions allow you to encapsulate and organize your code, making it easier to read, debug, and maintain.

# Here's the basic syntax for defining a function in Python:


# def function_name(arg1, arg2, ...):
#    # code to be executed
#    return value

# def is the keyword used to define a function.
# function_name is the name of the function. It should follow the same rules as variable names in Python.
# arg1, arg2, ... are the arguments (inputs) that the function takes. They are optional, and you can define as many or as few arguments as you need.
# The code inside the function is indented and is executed whenever the function is called.
# The return statement is used to return a value from the function. The function execution stops when a return statement is encountered.
# Here's an example of a function in Python:


def greet(name):
   message = "Hello, " + name + "!"
   return message

greeting = greet("John")
print(greeting)
# This code defines a function greet that takes a single argument name and returns a message that greets the person. The function is then called and the returned value is assigned to a variable greeting which is then printed. The output of the code will be:

# Hello, John!
# You can also define functions that take multiple arguments, like this:



def add(a, b):
   return a + b

sum = add(2, 3)
print(sum)
# This code defines a function add that takes two arguments a and b and returns the sum of the two numbers. The function is then called and the returned value is assigned to a variable sum which is then printed. The output of the code will be:
# 5


# https://youtube.com/@codewithmuh
# https://github.com/rashiddaha

