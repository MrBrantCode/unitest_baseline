"""
QUESTION:
Create a function named `sort_dict_list` that takes a list of dictionaries as input and returns the list sorted in ascending order based on a specific key. The dictionaries have a common key 'age'. The function should be able to sort the list based on the 'age' key.
"""

def sort_dict_list(animals):
    sorted_animals = sorted(animals, key=lambda k: k['age'])  
    return sorted_animals