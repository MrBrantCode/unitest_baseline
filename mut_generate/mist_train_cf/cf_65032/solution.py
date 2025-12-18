"""
QUESTION:
Create a function `is_lexicographically_descending_structure` that takes a list of characters and/or nested lists as input and returns `True` if the list is arranged in lexicographically descending sequence, and `False` otherwise. The function should be able to handle potentially hundreds of thousands of data points efficiently.
"""

def is_lexicographically_descending_structure(data):
    # Verify if data is list type
    if not isinstance(data, list):
        return False
      
    # Flattens a list of strings and lists
    def flatten_data(s):
        if s == []:
            return s
        if isinstance(s[0], list):
            return flatten_data(s[0]) + flatten_data(s[1:])
        return s[:1] + flatten_data(s[1:])

    flattened_data = flatten_data(data)

    # Compare the original list with its copy sorted in descending order
    return flattened_data == sorted(flattened_data, reverse=True)