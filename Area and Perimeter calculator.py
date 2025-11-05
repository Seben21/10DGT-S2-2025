# Author: Zach Fryer
# Title: Area/Perimeter Calculator
# Date: 31/10/2025
# Version 1.7

print("Hello User, welcome to my Area/Perimeter calculator! \nPlease answer the following questions so I can calculate for you!") # Introduction
repeat = ""
while repeat == "":
    try:
        dimensions = input("\n\nIs your shape 2D or 3D? ").lower() # Get dimensions required
        if dimensions == "2d":
            while True:
                try:
                    length = float(input(f"Please enter the length of the shape in cm: ")) # Get length 2d
                    if length <= 0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                try:
                    width = float(input(f"Please enter the width of the shape in cm: ")) # Get width 2d
                    if width <=0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                area = length * width # Calculate area
                perimeter = 2 * (length + width) # Calculate perimeter
                print(f"Area = {area} cm²\nPerimeter = {perimeter} cm\n\n")
                break
            repeat = input("Would you like to continue?\nPress <ENTER> to repeat:  ") # Loop
        elif dimensions == "3d":
            while True:
                try:
                    length = float(input(f"Please enter the length of the shape in cm: ")) # Get length 3d
                    if length <= 0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                try:
                    width = float(input(f"Please enter the width of the shape in cm: ")) # Get width 3d
                    if width <=0:
                        print("Please enter a number above 0\n")
                    else:
                        break
                except ValueError:
                    print(f"Please enter a value\n")
            print()
            while True:
                        try:
                            height = float(input(f"Please enter the height of the shape in cm: ")) # Get height 3d
                            if height <=0:
                                print("Please enter a number above 0\n")
                            else:
                                break
                        except ValueError:
                            print(f"Please enter a value\n")
            print()
            while True:
                surface_area = 2 * (height*width + width*length + length*height) # Calculate surface area
                volume = length * height * width # Calculate volume
                print(f"Surface Area = {surface_area} cm²\nVolume = {volume} cm³\n\n")
                break
            repeat = input("Would you like to continue?\nPress <ENTER> to repeat:  ") # Loop
        else:
            print("ERROR - Please enter either <2D> or <3D>!!!! \n") 
    except ValueError:
        repeat = ''
        print("\n")