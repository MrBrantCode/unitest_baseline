"""
QUESTION:
Write a function `get_preceding_student_age` that takes a list of dictionaries representing students and a hobby as input, and returns the age of the student preceding the one whose second hobby matches the given hobby. The list of dictionaries contains keys 'name', 'age', and 'hobbies' where 'hobbies' is a list of strings. If no match is found, the function should return None.
"""

def get_preceding_student_age(student_data, hobby):
    for i in range(1, len(student_data)):
        if len(student_data[i]['hobbies']) > 1 and hobby == student_data[i]['hobbies'][1]:
            return student_data[i - 1]['age']
    return None