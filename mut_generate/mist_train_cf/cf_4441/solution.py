"""
QUESTION:
Create a function called `validate_dictionary` that takes a dictionary as input and returns True if it meets the following conditions: 
- The dictionary contains the keys 'name', 'age', and 'occupation'.
- The 'name' value is a string with a minimum length of 3 characters.
- The 'age' value is an integer between 18 and 40 (inclusive).
- The 'occupation' value is a string with a minimum length of 5 characters and is one of the following: 'student', 'teacher', 'engineer', 'doctor'. 
If any condition is not met, the function should return False.
"""

def validate_dictionary(dictionary):
    if 'name' in dictionary and 'age' in dictionary and 'occupation' in dictionary:
        if type(dictionary['name']) == str and len(dictionary['name']) >= 3:
            if type(dictionary['age']) == int and 18 <= dictionary['age'] <= 40:
                if type(dictionary['occupation']) == str and len(dictionary['occupation']) >= 5:
                    occupations = ['student', 'teacher', 'engineer', 'doctor']
                    if dictionary['occupation'] in occupations:
                        return True
    return False