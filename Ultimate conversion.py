# Ultimate conversion
# Author: Zach Fryer
# Date: 21/11/2025
# Version 3.0

def length_multiplication():
    if first_length == 1 and second_length == 1:
        print(f"The converted value of {f_l_amount}mm to mm equals {f_l_amount}mm")
    elif first_length == 1 and second_length == 2:
        print(f"The converted value of {f_l_amount}mm to cm equals {f_l_amount / 10}cm")
    elif first_length == 1 and second_length == 3:
        print(f"The converted value of {f_l_amount}mm to m equals {f_l_amount / 1000}m")
    elif first_length == 1 and second_length == 4:
        print(f"The converted value of {f_l_amount}mm to km equals {f_l_amount / 1000000}km")
    elif first_length == 2 and second_length == 1:
        print(f"The converted value of {f_l_amount}cm to mm equals {f_l_amount*10}mm")
    elif first_length == 2 and second_length == 2:
        print(f"The converted value of {f_l_amount}cm to cm equals {f_l_amount}cm")
    elif first_length == 2 and second_length == 3:
        print(f"The converted value of {f_l_amount}cm to m equals {f_l_amount / 100}m")
    elif first_length == 2 and second_length == 4:
        print(f"The converted value of {f_l_amount}cm to km equals {f_l_amount / 10000}km")
    elif first_length == 3 and second_length == 1:
        print(f"The converted value of {f_l_amount}m to mm equals {f_l_amount*1000}mm")
    elif first_length == 3 and second_length == 2:
        print(f"The converted value of {f_l_amount}m to cm equals {f_l_amount*100}cm")
    elif first_length == 3 and second_length == 3:
        print(f"The converted value of {f_l_amount}m to m equals {f_l_amount}m")
    elif first_length == 3 and second_length == 4:
        print(f"The converted value of {f_l_amount}m to km equals {f_l_amount / 1000}km")
    elif first_length == 4 and second_length == 1:
        print(f"The converted value of {f_l_amount}km to mm equals {f_l_amount*1000000}mm")
    elif first_length == 4 and second_length == 2:
        print(f"The converted value of {f_l_amount}km to cm equals {f_l_amount*100000}cm")
    elif first_length == 4 and second_length == 3:
        print(f"The converted value of {f_l_amount}km to m equals {f_l_amount*1000}m")
    elif first_length == 4 and second_length == 4:
        print(f"The converted value of {f_l_amount}km to km equals {f_l_amount}km")
    else:
        print("Error")

def weight_multiplication():
    if first_weight == 1 and second_weight == 1:
        print(f"The converted value of {f_w_amount}mg to mg equals {f_w_amount}mg")
    elif first_weight == 1 and second_weight == 2:
        print(f"The converted value of {f_w_amount}mg to g equals {f_w_amount / 10}g")
    elif first_weight == 1 and second_weight == 3:
        print(f"The converted value of {f_w_amount}mg to kg equals {f_w_amount / 1000}kg")
    elif first_weight == 1 and second_weight == 4:
        print(f"The converted value of {f_w_amount}mg to t equals {f_w_amount / 1000000}t")
    elif first_weight == 2 and second_weight == 1:
        print(f"The converted value of {f_w_amount}g to mm equals {f_w_amount*10}mg")
    elif first_weight == 2 and second_weight == 2:
        print(f"The converted value of {f_w_amount}g to g equals {f_w_amount}g")
    elif first_weight == 2 and second_weight == 3:
        print(f"The converted value of {f_w_amount}g to kg equals {f_w_amount / 100}kg")
    elif first_weight == 2 and second_weight == 4:
        print(f"The converted value of {f_w_amount}g to t equals {f_w_amount / 10000}t")
    elif first_weight == 3 and second_weight == 1:
        print(f"The converted value of {f_w_amount}kg to mg equals {f_w_amount*1000}mg")
    elif first_weight == 3 and second_weight == 2:
        print(f"The converted value of {f_w_amount}kg to g equals {f_w_amount*100}g")
    elif first_weight == 3 and second_weight == 3:
        print(f"The converted value of {f_w_amount}kg to kg equals {f_w_amount}kg")
    elif first_weight == 3 and second_weight == 4:
        print(f"The converted value of {f_w_amount}kg to t equals {f_w_amount / 1000}t")
    elif first_weight == 4 and second_weight == 1:
        print(f"The converted value of {f_w_amount}t to mg equals {f_w_amount*1000000}mg")
    elif first_weight == 4 and second_weight == 2:
        print(f"The converted value of {f_w_amount}t to g equals {f_w_amount*100000}g")
    elif first_weight == 4 and second_weight == 3:
        print(f"The converted value of {f_w_amount}t to kg equals {f_w_amount*1000}kg")
    elif first_weight == 4 and second_weight == 4:
        print(f"The converted value of {f_w_amount}t to t equals {f_w_amount}t")
    else:
        print("Error")

def time_multiplication():
    if first_time == 1 and second_time == 1:
        print(f"The converted value of {f_t_amount}ms to ms equals {f_t_amount}ms")
    elif first_time == 1 and second_time == 2:
        print(f"The converted value of {f_t_amount}ms to s equals {f_t_amount / 100}s")
    elif first_time == 1 and second_time == 3:
        print(f"The converted value of {f_t_amount}ms to m equals {f_t_amount / 60000}mins")
    elif first_time == 1 and second_time == 4:
        print(f"The converted value of {f_t_amount}ms to h equals {f_t_amount / 3600000}h")
    elif first_time == 2 and second_time == 1:
        print(f"The converted value of {f_t_amount}s to ms equals {f_t_amount*100}ms")
    elif first_time == 2 and second_time == 2:
        print(f"The converted value of {f_t_amount}s to s equals {f_t_amount}s")
    elif first_time == 2 and second_time == 3:
        print(f"The converted value of {f_t_amount}s to m equals {f_t_amount / 60}mins")
    elif first_time == 2 and second_time == 4:
        print(f"The converted value of {f_t_amount}s to h equals {f_t_amount / 3600}h")
    elif first_time == 3 and second_time == 1:
        print(f"The converted value of {f_t_amount}m to ms equals {f_t_amount*60000}ms")
    elif first_time == 3 and second_time == 2:
        print(f"The converted value of {f_t_amount}m to s equals {f_t_amount*60}s")
    elif first_time == 3 and second_time == 3:
        print(f"The converted value of {f_t_amount}m to m equals {f_t_amount}mins")
    elif first_time == 3 and second_time == 4:
        print(f"The converted value of {f_t_amount}m to h equals {f_t_amount / 60}h")
    elif first_time == 4 and second_time == 1:
        print(f"The converted value of {f_t_amount}h to ms equals {f_t_amount*3600000}ms")
    elif first_time == 4 and second_time == 2:
        print(f"The converted value of {f_t_amount}h to s equals {f_t_amount*3600}s")
    elif first_time == 4 and second_time == 3:
        print(f"The converted value of {f_t_amount}h to m equals {f_t_amount*60}mins")
    elif first_time == 4 and second_time == 4:
        print(f"The converted value of {f_t_amount}h to h equals {f_t_amount}h")
    else:
        print("Error")
keep_going = ""
input("Hello user, welcome to my ultimate conversion calculator! Press enter to continue: ")
while keep_going == "":
    type = int(input("\n\n\nWhat type of conversion would you like to do?\nEnter 1 for Length conversion: \nEnter 2 for Mass conversion: \nEnter 3 for Time conversion: \n"))
    if type == 1:
        print()
        first_length = int(input("What is your starting value?\nPress 1 for milimetres\nPress 2 for centimetres\nPress 3 for metres\nPress 4 for kilometres\n"))
        if first_length == 1:
            f_l_amount = float(input("How long is it in milimetres? "))
            second_length = int(input("\nWhat are you converting it to?\nPress 1 for milimetres\nPress 2 for centimetres\nPress 3 for metres\nPress 4 for kilometres\n\n"))
            length_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_length == 2:
            f_l_amount = float(input("How long is it in centimetres? "))
            second_length = int(input("What are you converting it to?\nPress 1 for milimetres\nPress 2 for centimetres\nPress 3 for metres\nPress 4 for kilometres\n"))
            length_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_length == 3:
            f_l_amount = float(input("How long is it in metres? "))
            second_length = int(input("What are you converting it to?\nPress 1 for milimetres\nPress 2 for centimetres\nPress 3 for metres\nPress 4 for kilometres\n"))
            length_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_length == 4:
            f_l_amount = float(input("How long is it in kilometres? "))
            second_length = int(input("What are you converting it to?\nPress 1 for milimetres\nPress 2 for centimetres\nPress 3 for metres\nPress 4 for kilometres\n"))
            length_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        else:
            print("Error")
    elif type == 2:
        print()
        first_weight = int(input("What is your starting value?\nPress 1 for miligrams\nPress 2 for grams\nPress 3 for kilograms\nPress 4 for tonnes\n"))
        if first_weight == 1:
            f_w_amount = float(input("How heavy is it in miligrams? "))
            second_weight = int(input("What are you converting it to?\nPress 1 for miligrams\nPress 2 for grams\nPress 3 for kiligrams\nPress 4 for tonnes\n"))
            weight_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_weight == 2:
            f_w_amount = float(input("How heavy is it in grams? "))
            second_weight = int(input("What are you converting it to?\nPress 1 for miligrams\nPress 2 for grams\nPress 3 for kiligrams\nPress 4 for tonnes\n"))
            weight_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_weight == 3:
            f_w_amount = float(input("How heavy is it in kilograms? "))
            second_weight = int(input("What are you converting it to?\nPress 1 for miligrams\nPress 2 for grams\nPress 3 for kiligrams\nPress 4 for tonnes\n"))
            weight_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_weight == 4:
            f_w_amount = float(input("How heavy is it in tonnes? "))
            second_weight = int(input("What are you converting it to?\nPress 1 for miligrams\nPress 2 for grams\nPress 3 for kiligrams\nPress 4 for tonnes\n"))
            weight_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        else:
            print("Error")
    elif type == 3:
        print()
        first_time = int(input("What is your starting value?\nPress 1 for miliseconds\nPress 2 for seconds\nPress 3 for minutes\nPress 4 for hours\n"))
        if first_time == 1:
            f_t_amount = float(input("How long is it in miliseconds? "))
            second_time = int(input("What are you converting it to?\nPress 1 for miliseconds\nPress 2 for seconds\nPress 3 for minutes\nPress 4 for hours\n"))
            time_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_time == 2:
            f_t_amount = float(input("How long is it in seconds? "))
            second_time = int(input("What are you converting it to?\nPress 1 for miliseconds\nPress 2 for seconds\nPress 3 for minutes\nPress 4 for hours\n"))
            time_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_time == 3:
            f_t_amount = float(input("How long is it in minutes? "))
            second_time = int(input("What are you converting it to?\nPress 1 for miliseconds\nPress 2 for seconds\nPress 3 for minutes\nPress 4 for hours\n"))
            time_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        elif first_time == 4:
            f_t_amount = float(input("How long is it in hours? "))
            second_time = int(input("What are you converting it to?\nPress 1 for miliseconds\nPress 2 for seconds\nPress 3 for minutes\nPress 4 for hours\n"))
            time_multiplication()
            keep_going = input("Press enter to repeat\nPress anything else to finish  ")
        else:
            print("Error")
    else:
        print("Error")
print("\n\nThank you for using this conversion calculator!")