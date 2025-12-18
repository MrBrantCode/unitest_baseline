"""
QUESTION:
Create a function named `sort_dictionaries` that takes a list of dictionaries as input and returns a sorted list. The sorting should be done in descending order of the length of the string value for the key "name" and in ascending order of the numerical value for the key "age" in case of a tie.
"""

def sort_dictionaries(lst):
    return sorted(lst, key=lambda x: (-len(x["name"]), x["age"]))