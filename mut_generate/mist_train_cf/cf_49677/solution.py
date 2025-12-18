"""
QUESTION:
Create a function `celebrate_birthday(name, age)` that prints a birthday message with the correct age suffix ("th" is used for all ages in this case) and only accepts age values within the range of 1-123. If the inputted age is out of this range, return an error message "Error: Age must be between 1 and 123."
"""

def celebrate_birthday(name, age):
    if age < 1 or age > 123:
        return "Error: Age must be between 1 and 123."

    print("Happy " + str(age) + "th Birthday, " + name)