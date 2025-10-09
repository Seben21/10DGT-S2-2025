# Author: Zach Fryer
# Date: 10/10/2025
# Create a chatbot that covinces people to like coffee

# Ask the user if they like coffee - Version 1.0
'''like_coffee = input("Do you like coffee? ")
print('Your answer was',like_coffee)

if like_coffee == "Yes":
    print("That's great! I like coffee too.")
else:
    print("You are misssing out! Why not give it a try?")'''

# While loop - Version 2.0
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")

    if like_coffee == "Yes":
        print("That's great! I like coffee too.")
        keep_going = "Yes"
    elif like_coffee == "No":
        print("You are misssing out! Why not give it a try?")
    else:
        print("Error, please type either Yes or No")