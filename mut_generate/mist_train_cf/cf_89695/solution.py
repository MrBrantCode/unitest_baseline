"""
QUESTION:
Create a function called `calculate_sum` that takes a dictionary as input and returns the sum of all the values in the dictionary, excluding any negative values. The dictionary will have unique keys and values that are random integers between -100 and 100, with no duplicate values.
"""

def calculate_sum(dictionary):
    sum = 0
    for value in dictionary.values():
        if value > 0:
            sum += value
    return sum