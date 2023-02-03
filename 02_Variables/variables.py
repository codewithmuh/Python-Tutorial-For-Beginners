# Python Tutorial 

#Variables store data in a computer Memory.

# A Python, a variable is a named location in memory used to store a value. When you create a variable, you specify
# its name and the value it should store. You can then access the value stored in a variable by referencing its name.

# In Python, you can create variables of different types, such as integers, floating point numbers, and strings.
# The type of a variable is determined by the value it stores.

# Let’s  jump into computer screen.


# Python is a case-sensitive programming language. This means that it treats uppercase 
# and lowercase letters differently.
# Hence, we cannot use two terms having same characters but different cases interchangeably in Python.

x= 5
print('x')

y="Hello World"
z= 12.5



# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Code With', 'Muh', 'Pakistan', 23, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)



###


first_name = 'Code with'
last_name = 'Muh'
country = 'Pakistan'
city = 'Isb'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'David', 
    'lastname':'Da', 
    'country':'Pakistan',
    'city':'Isb'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)