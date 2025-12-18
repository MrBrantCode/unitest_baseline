"""
QUESTION:
Write a function `calculate_average_age` that takes a list of tuples as input, where each tuple contains a person's name and age. The list should have at least 5 elements and the names should be unique. Each person's age should be between 18 and 60. The function should return the average age of the people in the list.
"""

def calculate_average_age(persons):
    total_age = sum(age for _, age in persons)
    return total_age / len(persons)