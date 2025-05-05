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