# Author: Zach Fryer
# Title: Area/Perimeter Calculator
# Date: 29/10/2025
# Version 1.3

print("Hello User, welcome to my Area/Perimeter calculator! \nPlease answer the following questions so I can calculate for you!\n\n")
dimensions = input("Is your shape 2D or 3D? ").lower()
repeat = ""
while repeat == "":
    if dimensions == "2d":
        while True:
            try:
                length = float(input(f"Please enter the length of the shape: "))
                if length <= 0:
                    print("Please enter a number above 0\n")
                else:
                    break
            except ValueError:
                print(f"Please enter a value\n")
        print()
        while True:
            try:
                width = float(input(f"Please enter the width of the shape: "))
                if width <=0:
                    print("Please enter a number above 0\n")
                else:
                    break
            except ValueError:
                print(f"Please enter a value\n")
        print()
        while True:
            area = length * width
            perimeter = length * 2 + width * 2
            print(f"Area = {area}\nPerimeter = {perimeter}\n\n")
            break
        repeat = input("Would you like to continue?\nPress any key to continue,\nPress <ENTER> to repeat:  ")
    
    elif dimensions == "3d":
        while True:
            try:
                length = float(input(f"Please enter the length of the shape: "))
                if length <= 0:
                    print("Please enter a number above 0\n")
                else:
                    break
            except ValueError:
                print(f"Please enter a value\n")
        print()
        while True:
            try:
                width = float(input(f"Please enter the width of the shape: "))
                if width <=0:
                    print("Please enter a number above 0\n")
                else:
                    break
            except ValueError:
                print(f"Please enter a value\n")
        print()
        while True:
                    try:
                        height = float(input(f"Please enter the width of the shape: "))
                        if height <=0:
                            print("Please enter a number above 0\n")
                        else:
                            break
                    except ValueError:
                        print(f"Please enter a value\n")
        print()
        while True:
            surface_area = 2 * (height*width + width*length + length*height)
            volume = length * height * width
            print(f"Surface Area = {surface_area}\nVolume = {volume}\n\n")
            break
        repeat = input("Would you like to continue?\nPress any key to continue,\nPress <ENTER> to repeat:  ")