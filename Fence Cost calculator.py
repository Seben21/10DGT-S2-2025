# Author: Zach Fryer
# Title: Fence cost calculator
# Date: 7/11/2025
# Version 1.7

print("Hello User, welcome to my fence cost calculator!\nPlease answer all the following questions so I can calculate for you:") # Introduction
# Making the program loop if repeat equals nothing
repeat = ''
while repeat == '':
    while True: # Repeating cost per metre if they enter 0
        try:
            fence_cost_m = float(input("\n\nWhat is the cost per metre of said fence? $")) # Getting the cost per metre of fence - will be used to times against perimeter
            if fence_cost_m <= 0: # Checking if they entered a number above 0
                print("Please enter a value above 0") # Will make the question repeat if they don't enter a number above 0
            else: 
                break 
        except ValueError: # Checking if they entered a valid value (Float or Interger)
            print("Please enter a number") 
    while True:
        try:
            width = float(input("\nWhat is the width of the desired area to be fenced, in metres? ")) # Getting width so we can times width by length to get perimeter
            if width <= 0: # Checking if they entered a number above 0
                print("Please enter a value above 0") # Will make the question repeat if they don't enter a number above 0
            else: 
                break 
        except ValueError: # Checking if they entered a valid value (Float or Interger)
            print("Please enter a number") 
    while True:
        try:
            length = float(input("\nWhat is the length of the desired area to be fenced, in metres? ")) # Getting length, to times it against width to get perimeter
            if length <= 0: # Will make the question repeat if they don't enter a number above 0
                print("Please enter a value above 0")
            else: 
                break 
        except ValueError: # Checking if they have entered a valid value (Float or Interger)
            print("Please enter a number")
    print()
    perimeter = (width + length) * 2 # Calculate perimeter to times against cost_per_metre
    total_cost = perimeter * fence_cost_m # Calculate the total cost
    print(f"\n\nThe total price to fully fence the entire area is ${total_cost} ")
    repeat = input("\n\nPress any key to end the program\nPress <ENTER> if you wish to repeat: ") # Loop program
print("Thank you for using this calculator") # Ending note - Thanks for using this calculator