# Task 1
def find_bigger(a, b):
    """This is a simple function taking 2 ints as arguments and returning the greater og them."""
    return a if a > b else b

find_bigger(1, 2)

# Task 2
import math
def triangle_area():
    base = int(input("Enter your base in cm: "))
    height_to_base = int(input("Enter the height to base in cm: "))
    area = height_to_base * base / 2
    print(area)

def rectangle_area():
    a = int(input("Enter one side length: "))
    b = int(input("Enter another side length: "))
    area = a * b
    print(area)

def circle_area():
    radius = int(input("Enter your radius: "))
    area = math.pi * radius ** 2
    print(round(area,1))

def calculate_area():
    """This is a wrap-up function that allows to calculate the area of a user-chosen figure"""
    figure = input("Please enter a figure you want to calculate the area of: ")
    match figure:
        case "triangle":
            return triangle_area()
        case "rectangle":
            return rectangle_area()
        case "circle":
            return circle_area()
        case _:
            print("Please verify your input! Enter either triangle, circle, or rectangle.")

calculate_area()


# Task 3

def find_number_of_characters(strn):
    enumerated = {}
    for char in strn:
        count = strn.count(char)
        enumerated.update({char:count})
    print(enumerated)

find_number_of_characters("hello")