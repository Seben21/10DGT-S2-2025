# Author: Zach Fryer
# Date: 10/10/2025
# Create a chatbot that covinces people to like coffee
# Version 1.0

# TODO: Ask the user if they like coffee
#       record their answer
#       Give a response back

# Ask the user if they like coffee
like_coffee = input("Do you like coffee? ")
print('Your answer was',like_coffee)

if like_coffee == "Yes":
    print("That's great! I like coffee too.")
else:
    print("You are misssing out! Why not give it a try?")