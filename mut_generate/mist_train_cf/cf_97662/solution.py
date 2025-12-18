"""
QUESTION:
Create a function called `check_eligibility` that takes a JSON object as input. The JSON object contains two keys: "age" (an integer) and "grades" (a list of strings). The function should return "Congratulations, you are eligible for acceptance!" if the age is 18 or older and all grades are "A", and "Sorry, you are not eligible for acceptance." otherwise.
"""

import json

def check_eligibility(data):
    """
    This function checks if a person is eligible for acceptance into a prestigious university based on their age and recent grades.
    
    Args:
        data (dict): A dictionary containing the person's age and grades.
        
    Returns:
        str: A message indicating whether the person is eligible for acceptance.
    """
    if data["age"] >= 18 and all(grade == "A" for grade in data["grades"]):
        return "Congratulations, you are eligible for acceptance!"
    else:
        return "Sorry, you are not eligible for acceptance."