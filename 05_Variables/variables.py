# Python Tutorial 2023
# Video #05  - # Variables in Python

#Variables store data in a computer Memory.

#A Python, a variable is a named location in memory used to store a value. When you create a variable, you specify
# its name and the value it should store. You can then access the value stored in a variable by referencing its name.

#In Python, you can create variables of different types, such as integers, floating point numbers, and strings.
# The type of a variable is determined by the value it stores.

#Let’s  jump into computer screen.

x= 5
print('x')

y="Hello World"
z= 12.5



# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)



###


first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
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