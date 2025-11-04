# Author: Zach Fryer
# Title: Area/Perimeter Calculator
# Date: 31/10/2025
# Version 1.6

print("Hello User, welcome to my Area/Perimeter calculator! \nPlease answer the following questions so I can calculate for you!")
repeat = ""
while repeat == "":
    try:
        dimensions = input("\n\nIs your shape 2D or 3D? ").lower()
        if dimensions == "2d":
            while True:
                try:
                    length = float(input(f"Please enter the length of the shape in cm: "))
                    if length <= 0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                try:
                    width = float(input(f"Please enter the width of the shape in cm: "))
                    if width <=0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                area = length * width
                perimeter = 2 * (length + width)
                print(f"Area = {area} cm²\nPerimeter = {perimeter} cm\n\n")
                break
            repeat = input("Would you like to continue?\nPress <ENTER> to repeat:  ")
        elif dimensions == "3d":
            while True:
                try:
                    length = float(input(f"Please enter the length of the shape in cm: "))
                    if length <= 0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                try:
                    width = float(input(f"Please enter the width of the shape in cm: "))
                    if width <=0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                        try:
                            height = float(input(f"Please enter the height of the shape in cm: "))
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
                print(f"Surface Area = {surface_area} cm²\nVolume = {volume} cm³\n\n")
                break
            repeat = input("Would you like to continue?\nPress <ENTER> to repeat:  ")
        else:
            print("ERROR - Please enter either <2D> or <3D>!!!! \n")
    except ValueError:
        repeat = ''
        print("\n")