from math import pow, pi

import area_functions

def choose_figure(input):
    match input:
        case "circle":
            area_functions.circle_area()
        case "rectangle":
            area_functions.rectangle_area()
        case "triangle":
            area_functions.triangle_area()
        case _:
            print("Please verify your input: type either circle, rectangle, ot triangle!")


choose_figure(input("Enter a figure you want to calculate area of: "))