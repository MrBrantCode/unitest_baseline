"""
QUESTION:
Create a function named `updateValue` that takes a dictionary, a key, and a value as parameters. If the key already exists in the dictionary, update its value by appending the new value to the old value with a hyphen in between. If the key does not exist, assign the new value to the key. The function should return the updated dictionary.
"""

def updateValue(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += '-' + value
    else:
        dictionary[key] = value
    return dictionary