"""
QUESTION:
Create a function `filter_dictionaries` that takes three parameters: an integer, a string, and a list of dictionaries. The function should return a new list containing only the dictionaries from the input list that have a key-value pair where the key is the integer and the value is the string.
"""

def filter_dictionaries(key, value, dictionaries):
    return [dictionary for dictionary in dictionaries if dictionary.get(key) == value]