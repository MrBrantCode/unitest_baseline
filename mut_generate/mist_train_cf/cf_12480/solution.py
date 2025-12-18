"""
QUESTION:
Write a function `find_highest_priority_object` that takes an array of objects as input, where each object contains 'name', 'age', 'weight', and 'birthdate'. Return the 'name' of the object with the highest 'age', and in case of a tie, prioritize 'weight', then 'birthdate' (earlier is higher priority), and finally 'name' (shorter is higher priority).
"""

def find_highest_priority_object(objects):
    return max(objects, key=lambda x: (x['age'], x['weight'], x['birthdate'], len(x['name'])))['name']