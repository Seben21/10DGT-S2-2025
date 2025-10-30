# Author: Zach Fryer
# Title: Fence cost calculator
# Date: 31/10/2025
# Version 1.0

print("Hello User, welcome to my fence cost calculator!\nPlease answer all the following questions so I can calculate for you:\n")
repeat = ''
while repeat == '':
    try:
        fence_cost = float(input("What is the cost per metre of said fence? "))
        width = float(input("\nWhat is the width of the desired area to be fenced, in metres? "))
        length = float(input("\nWhat is the length of the desired area to be fenced, in metres? "))

        perimeter = (width + length) * 2
        total_cost = perimeter * fence_cost
        print(f"\n\nThe total price for the fence is ${total_cost} ")
        repeat = input("\n\nPress <ENTER> if you wish to repeat: ")
    except ValueError:
        print("\nThats not a valid value")