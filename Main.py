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

''' # While loop - Version 2.0
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? ")

    if like_coffee == "Yes":
        print("That's great! I like coffee too.")
        keep_going = "Yes"
    elif like_coffee == "No":
        print("You are misssing out! Why not give it a try?")
    else:
        print("Error, please type either Yes or No") '''

def coffee_program():
    keep_going = ""
    while keep_going == "":
        like_coffee = input("Do you like coffee? ").lower()
        if like_coffee == "yes" or like_coffee == "y":
            print("Thats great, I like coffee too!")
        elif like_coffee == "no" or like_coffee == "n":
            print("Thats too bad")
            like_tea = input("Do you like tea instead? ").lower()
            if like_tea == "yes" or like_tea == "y":
                print("Good for you")
            elif like_tea == "no" or like_tea == "n":
                print("You picky little ****, do you even like anything???")
        else:
            print("I don't understand. Please answer with either a yes or a no.")
    
        keep_going = input("Press any key to continue. Press <Enter> to repeat.")

if __name__ == "__main__":
    coffee_program()