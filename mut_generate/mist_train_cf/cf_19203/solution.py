"""
QUESTION:
Create a function named `create_person_dict` that takes three parameters: `name`, `age`, and `occupation`. The function should return a dictionary with these three elements if the values meet the following conditions: `name` is a string with a minimum length of 3 characters, `age` is an integer between 18 and 40 (inclusive), and `occupation` is a string with a minimum length of 5 characters and one of the following: 'student', 'teacher', 'engineer', 'doctor'. If the values do not meet these conditions, the function should return None.
"""

def create_person_dict(name, age, occupation):
    valid_occupations = ['student', 'teacher', 'engineer', 'doctor']
    if (isinstance(name, str) and len(name) >= 3 and 
        isinstance(age, int) and 18 <= age <= 40 and 
        isinstance(occupation, str) and len(occupation) >= 5 and occupation in valid_occupations):
        return {'name': name, 'age': age, 'occupation': occupation}
    else:
        return None