# Task 1

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


# Task 2

def day_of_week(number):
    try:
        number = int(number)
        match number:
            case "1":
                return "Monday"
            case "2":
                return "Tuesday"
            case "3":
                return "Wednesday"
            case "4":
                return "Thursday"
            case "5":
                return "Friday"
            case "6":
                return "Saturday"
            case "7":
                return "Sunday"
            case _:
                print("Only numbers 1 to 7 are allowed!")
    except ValueError as e:
       print("Must be a number!")


day_number = input("Please enter the day number here: ")
day_of_week(day_number)


