#In programming, an operator is a symbol that performs a specific operation
# on one or more operands (values or variables). For example, in the 
# expression "4 + 5", the + symbol is the operator that performs the
# addition operation. 

1.#Arithmetic operators
2. #Assignment operators
3. #Comparison operators
4. #Membership opertors

#Arithmetic operators
#Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

#For example:


x = 10
y = 5

# Addition
z = x + y  # z is 15

# Subtraction
z = x - y  # z is 5

# Multiplication
z = x * y  # z is 50

# Division
z = x / y  # z is 2.0

# Modulus (returns the remainder of a division)
z = x % y  # z is 0

# Exponentiation (raises a number to a power)
z = x ** y  # z is 100000

# Floor division (divides two numbers and rounds down to the nearest integer)
z = x // y  # z is 2

#Assignment operators
#Assignment operators are used to assign a value to a variable.


x = 10  # assigns the value 10 to the variable x

x += 5  # x is now 15 (same as x = x + 5)
x -= 5  # x is now 10 (same as x = x - 5)
x *= 5  # x is now 50 (same as x = x * 5)
x /= 5  # x is now 10 (same as x = x / 5)
x %= 5  # x is now 0 (same as x = x % 5)
x **= 5  # x is now 100000 (same as x = x ** 5)
x //= 5  # x is now 20000 (same as x = x // 5)

#Comparison operators
#Comparison operators are used to compare two values and return a Boolean value (True or False) based on the comparison.


x = 10
y = 5

# Equal to
z = x == y  # z is False

# Not equal to
z = x != y  # z is True

# Greater than
z = x > y  # z is True

# Less than
z = x < y  # z is False

# Greater than or equal to
z = x >= y  # z is True

# Less than or equal to
z = x <= y  # z is False

#Logical operators
#Logical operators are used to perform logical operations such as AND, OR, and NOT.

#For example:

x = True
y = False

# AND
z = x and y  # z is False

# OR
z = x or y  # z is True

# NOT
z = not x  # z is False

#Membership operators
#Membership operators are used to test if a value is a member of a sequence (such as a list, tuple, or string).



x = "hello"
y = "world"
z = "hello"

# IN
a = x in y  # a is False
b = x in z  # b is True

# NOT IN
a = x not in y  # a is True
b = x not in z  # b is False

# https://youtube.com/@codewithmuh