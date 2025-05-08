# Task 1
import random

my_int_list = []
for times in range(10):
    my_int_list.append(random.randint(1, 100))

print(my_int_list)

my_float_list = [float(num) for num in my_int_list]
print(my_float_list)
print(" ")


# Task 2 Fibonacci
n = 50

a, b = 0, 1

for time in range(n):
    print(a, end=" ")
    a, b = b, a + b
print(" ")


# Task 3
print(" ")
number = int(input("Please enter the number yuou want the factorial of: "))
factorial = 0

for time in range(number):
    factorial += number * number-1
print(factorial)
