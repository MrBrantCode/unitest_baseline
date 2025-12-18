"""
QUESTION:
Write a function `extract_hobby_age` that takes a JSON object representing a list of students and returns the age of the second hobby of the first student. The JSON object has the following structure: a dictionary with a key "students" that maps to a list of dictionaries, each representing a student with keys "name", "age", and "hobbies". The "hobbies" key maps to a list of dictionaries, each representing a hobby with keys "name" and "years".
"""

def extract_hobby_age(data):
    """
    This function takes a JSON object representing a list of students and returns the age of the second hobby of the first student.

    Parameters:
    data (dict): A dictionary representing the JSON object.

    Returns:
    int: The age of the second hobby of the first student.
    """
    return data['students'][0]['hobbies'][1]['years']