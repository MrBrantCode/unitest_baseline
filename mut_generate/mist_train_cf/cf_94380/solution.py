"""
QUESTION:
Create a class "Person" with attributes "name" (string), "age" (integer between 1 and 100), and "height" (float between 1.0 and 2.5). Implement a function "calculate_average" that takes a list of "Person" objects and returns the average age of all people in the list, with a time complexity of O(n), where n is the number of people in the list.
"""

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

def calculate_average(people):
    total_age = 0
    num_people = len(people)

    for person in people:
        total_age += person.age

    return total_age / num_people