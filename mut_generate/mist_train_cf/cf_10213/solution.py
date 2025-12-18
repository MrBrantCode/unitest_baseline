"""
QUESTION:
Create a function `create_dictionary(lst)` that takes a list of tuples as input, where each tuple contains a string of length at most 10 and an integer between 1 and 1000 (inclusive). The function should return a dictionary where each key is a string from the input tuples, and each value is a list of integers. The dictionary should be sorted in descending order based on the sum of the values in each list. The input list will have at most 1000 tuples.
"""

def create_dictionary(lst):
    dictionary = {}

    # Build the dictionary
    for key, value in lst:
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    # Sort the dictionary based on the sum of the values
    dictionary = dict(sorted(dictionary.items(), key=lambda item: sum(item[1]), reverse=True))

    return dictionary