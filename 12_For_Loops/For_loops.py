# Here are some exercises you can try to practice using for loops in Python:

# Print the numbers from 1 to 10:


for num in range(1, 11):
   print(num)
#Print the sum of the numbers from 1 to 100:


sum = 0
for num in range(1, 101):
   sum += num
print(sum)
#Print the multiplication table for a given number:


num = 5
for i in range(1, 11):
   print(num, "x", i, "=", num*i)
#Print the elements of a list in reverse order:


fruits = ['apple', 'banana', 'cherry']
for fruit in reversed(fruits):
   print(fruit)
#Check if a number is prime:


num = 17
is_prime = True
for i in range(2, num):
   if num % i == 0:
      is_prime = False
      break
if is_prime:
   print(num, "is a prime number")
else:
   print(num, "is not a prime number")
#These exercises should help you get a better understanding of how for loops work in Python.