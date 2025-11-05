# Author: Zach Fryer
# Title: Fence cost calculator
# Date: 31/10/2025
# Version 1.6

print("Hello User, welcome to my fence cost calculator!\nPlease answer all the following questions so I can calculate for you:") # intro
repeat = ''
while repeat == '':
    while True:
        try:
            fence_cost = float(input("\n\nWhat is the cost per metre of said fence? ")) # Get cost
            if fence_cost <= 0:
                print("Please enter a value above 0")
            else: 
                break
        except ValueError:
            print("Please enter a number")
    while True:
        try:
            width = float(input("\nWhat is the width of the desired area to be fenced, in metres? ")) # Get width
            if width <= 0:
                print("Please enter a value above 0")
            else: 
                break
        except ValueError:
            print("Please enter a number")
    while True:
        try:
            length = float(input("\nWhat is the length of the desired area to be fenced, in metres? ")) # Get length
            if length <= 0:
                print("Please enter a value above 0")
            else: 
                break
        except ValueError:
            print("Please enter a number")
    print()
    perimeter = (width + length) * 2 # Calculate perimeter
    total_cost = perimeter * fence_cost # Calculate total
    print(f"\n\nThe total price to fully fence the entire area is ${total_cost} ")
    repeat = input("\n\nPress <ENTER> if you wish to repeat: ") # Loop program