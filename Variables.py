# Demonstrate how variables are created and how they work
# Author: Zach Fryer
# Date: 08-10-2025
# Version 2.0

# Different types of variables
# Store a string
greeting = "Hello User!"
print (greeting) 

# Store an interger
num_1 = 7
num_2 = 5
print (num_1)
print (num_2)

# Assign the value of one variable of one variable to another
num_1 = greeting
print (num_1) # Don't assign values to variables if the names do not truthfully represent them

''' Do calculations with variables and store the result
in another variable. I can now
press enter
as
many times as
I
like
'''

# Creating a new variable
num_3 = 5
num_4 = 18
sum_1 = num_3 + num_4
print(sum_1)

# Concatenation
sum_string1 = "18"
sum_string2 = "5"

sum2 = sum_string1 + sum_string2
print(sum2)

# Print formating
print(f"My calculation for adiing {num_3} and {num_4} together is {sum_1}")
