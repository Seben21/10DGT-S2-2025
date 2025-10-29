# Author: Zach Fryer
# Title: Area/Perimeter Calculator
# Date: 29/10/2025
# Version 1.0

print("Hello User, welcome to my Area/Perimeter calculator! \nPlease answer the following questions so I can calculate for you!\n\n")
dimensions = input("Is your shape 2D or 3D? ").lower()

if dimensions == "2d":
    length = float(input(f"Please enter the length of the shape: "))
    width = float(input(f"Please enter the width of the shape: "))
    area = length * width
    perimeter = length * 2 + width * 2
    print(f"Area = {area}\nPerimeter = {perimeter}")
    