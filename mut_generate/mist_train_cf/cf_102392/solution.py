"""
QUESTION:
Create a function `age_category` that determines the age category based on a given age. The function should print "You are an adult" if the age is between 18 and 65 (inclusive), "You are a senior citizen with a milestone age" if the age is greater than 65 and a multiple of 5, and "Invalid age entered" if the age is less than 0 or greater than 120.
"""

def age_category(age):
    if age >= 18 and age <= 65:
        return "You are an adult"
    elif age > 65 and age % 5 == 0:
        return "You are a senior citizen with a milestone age"
    elif age < 0 or age > 120:
        return "Invalid age entered"