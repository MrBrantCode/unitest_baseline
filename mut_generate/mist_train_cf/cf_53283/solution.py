"""
QUESTION:
Write a function `arrange_by_age` that takes a dictionary as a parameter where the dictionary's keys are strings and its values are dictionaries with 'name', 'age', and 'city' keys. The function should return a new dictionary that preserves the original structure but with its keys sorted in descending order of their corresponding 'age' values. If the input dictionary is empty, return 'The dictionary is empty.' If the input is not a dictionary, return 'Invalid data. Please provide a dictionary.'
"""

def arrange_by_age(user_data):
    if not isinstance(user_data, dict):
        return 'Invalid data. Please provide a dictionary.'
    if not user_data:
        return 'The dictionary is empty.'
    # sort dictionary by 'age' in descending order
    sorted_data = dict(sorted(user_data.items(), key=lambda item: item[1]['age'], reverse=True))
    return sorted_data