"""
QUESTION:
Write a function `get_eldest_hobby` that takes a list of dictionaries representing students with their hobbies and returns the name and age of the hobby with the longest duration from the eldest student. The function should handle erroneous age inputs by converting string ages to integers and should be able to parse hobby durations in the format 'X years' or 'Xth year'. The student with the highest integer age is considered the eldest. If there are multiple hobbies with the same longest duration, return any one of them.
"""

import re
import json

def get_eldest_hobby(students_data):
    """
    This function takes a list of dictionaries representing students with their hobbies 
    and returns the name and age of the hobby with the longest duration from the eldest student.

    Args:
        students_data (list): A list of dictionaries representing students with their hobbies.

    Returns:
        tuple: A tuple containing the name and age of the hobby with the longest duration from the eldest student.
    """

    # Convert the age which could be string to integer
    for record in students_data:
        if isinstance(record['studentAge'], str):
            record['studentAge'] = int(''.join(filter(str.isdigit, record['studentAge'])))

        # Convert hobby age which could be string to integer
        for hobby in record['hobbies']:
            if isinstance(hobby['hobbyAge'], str):
                hobby['hobbyAge'] = int(''.join(filter(str.isdigit, hobby['hobbyAge'])))

    # sort the data by student age
    sorted_data = sorted(students_data, key=lambda x: x['studentAge'], reverse=True)

    # getting the name and age of hobby which has the longest duration from the eldest student
    eldest = sorted_data[0]
    eldest_hobby = max(eldest['hobbies'], key=lambda x:x['hobbyAge'])

    return (eldest_hobby['hobbyName'], eldest_hobby['hobbyAge'])