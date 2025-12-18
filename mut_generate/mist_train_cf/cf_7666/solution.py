"""
QUESTION:
Write a function called `filter_keys` that takes a dictionary and a list as parameters. The function should return a new list containing the dictionary keys that are present in the list and contain only alphabetic characters. The returned list should be sorted in descending order. The function should have a time complexity of O(n*m) and a space complexity of O(n), where n is the number of keys in the dictionary and m is the length of the list.
"""

def filter_keys(dictionary, lst):
    return sorted([key for key in dictionary if key.isalpha() and key in lst], reverse=True)