# Error Checking
# Author: Zach Fryer
# Date 24/10/2025
# Version 1.4

# Code that tests whether a valid input is given
# Make the code more pythonic

def valid_num(question, low, high):
    error = f"That is not an interger between {low} and {high}. "
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                break # This stops the while loop
            else:
                print (f"{error}\n")
        except ValueError:
            print(f"{error}\n")
    return response # This makes the response available to be used

if __name__ == "__main__": 

    num_1 = valid_num("Enter a number between 1 and 10: ", 1, 10)
    print(f"You entered {num_1}\n")

    num_2 = valid_num("Enter a number between 15 and 25: ", 15, 25)
    print(f"You entered {num_2}\n")

    num_3 = valid_num("Enter a number between 70 and 90: ", 70, 90)
    print(f"You entered {num_3}\n")

