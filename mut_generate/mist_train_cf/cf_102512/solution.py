"""
QUESTION:
Function: categorize_age(age)

Write a function that takes an integer age as input and returns a string that categorizes the person's age. The categories are defined as follows:
- If the age is less than 12, return "You are a child."
- If the age is between 12 and 18 (inclusive), return "You are a teenager."
- If the age is between 19 and 29 (inclusive), return "You are a young adult."
- If the age is between 30 and 49 (inclusive), return "You are a middle-aged adult."
- If the age is between 50 and 69 (inclusive), return "You are a senior adult."
- If the age is 70 or above, return "You are an elderly person."

Restrictions: None
"""

def categorize_age(age):
    if age < 12:
        return "You are a child."
    elif age <= 18:
        return "You are a teenager."
    elif age <= 29:
        return "You are a young adult."
    elif age <= 49:
        return "You are a middle-aged adult."
    elif age <= 69:
        return "You are a senior adult."
    else:
        return "You are an elderly person."