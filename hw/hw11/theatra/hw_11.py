def odd_even_age(input_age):
    if input_age < 0:
        raise Exception("Age must be positive!")
    else:
        if input_age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")

try:
    age = int(input("Please enter your age here: "))
    odd_even_age(age)
except ValueError as e:
    print("Please enter a number!")