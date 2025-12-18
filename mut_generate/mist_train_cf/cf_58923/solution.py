"""
QUESTION:
Create a function `Adventure` that takes a user's choice as input and determines the next step in a choose-your-own-adventure story based on the user's decision. The story begins at a crossroads with two options: going to the forest or going to the town. If the user chooses to go to the forest, the game ends with a failure message. If the user chooses to go to the town, the game ends with a success message. If the user enters an invalid choice, the game prompts the user to enter a valid choice. The function should be part of a larger program that allows users to create a character with a name and profession before starting the adventure.
"""

def Adventure(choice):
    if choice == "1":
        return "You decide to go to the forest, but unfortunately you got lost."
    elif choice == "2":
        return "You decide to go to the town. You meet the town folks and they greet you warmly. Congratulations!"
    else:
        return "Invalid input. Please enter 1 or 2."