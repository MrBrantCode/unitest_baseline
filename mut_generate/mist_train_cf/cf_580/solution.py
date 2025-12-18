"""
QUESTION:
Implement a function named compare_by_age_descending that can sort a list of objects in descending order based on a specific attribute 'age'. The function should be used as a key in the sort() function.
"""

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

def compare_by_age_descending(person):
    return -person.age