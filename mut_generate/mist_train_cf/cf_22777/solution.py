"""
QUESTION:
Create a function `create_new_dictionary` that takes a dictionary as input and returns a new dictionary where the values are the keys and the keys are the values. The new dictionary should only include keys from the original dictionary that have an odd length. The solution should have a time complexity of O(n), where n is the number of key-value pairs in the input dictionary.
"""

def create_new_dictionary(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if len(key) % 2 != 0:  
            new_dictionary[value] = key
    return new_dictionary