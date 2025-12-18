"""
QUESTION:
Write a function called `find_second_hobby_age` that takes a list of dictionaries representing students with their hobbies. Each student dictionary contains a list of hobby dictionaries. The function should return the number of years the first student has been engaged in their second hobby. Assume that each student has at least two hobbies.
"""

def find_second_hobby_age(students):
    return students[0]['hobbies'][1]['hobbyAge']