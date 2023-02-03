# Exception handling in Python allows you to handle errors that may occur during the execution of your code. By using exception handling, you can ensure that your code continues to run even if an error occurs.

# Here's the basic syntax for exception handling in Python:


# try:
#    # code that may raise an exception
# except ExceptionType as variable:
#    # code to handle the exception
   
   
# The try block contains the code that may raise an exception.
# The except block contains the code to handle the exception if it occurs. ExceptionType is the type of exception you want to catch, such as ValueError, TypeError, etc. variable is a variable that will contain the exception object if an exception occurs.
# You can have multiple except blocks to handle different types of exceptions.

# For example:

try:
   num = int(input("Enter a number: "))
except ValueError:
   print("Invalid input. Not a number.")
# This code tries to convert the input from the user to an integer. 
# If the input is not a valid number, a ValueError exception will be raised,
# and the code in the except block will be executed to handle the exception.

# You can also use the finally block to specify code that must be executed 
# whether an exception occurs or not. The syntax for using a finally block is:

# try:
#    # code that may raise an exception
# except ExceptionType as variable:
#    # code to handle the exception
# finally:
    # code to be executed regardless of whether an exception occurred
   
# For example:

try:
   num = int(input("Enter a number: "))
except ValueError:
   print("Invalid input. Not a number.")
finally:
   print("This code will always be executed.")
# In this code, the finally block will always be executed, even if an exception
# occurs in the try block.




# https://youtube.com/@codewithmuh
# https://github.com/rashiddaha





