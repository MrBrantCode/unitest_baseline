"""
QUESTION:
Write a function `filter_names` that takes a list of names as input and returns a new list containing only the names that meet the following conditions: the name has more than 6 characters and the first character is the same as the last character.
"""

def filter_names(names):
    result = []
    for name in names:
        # Check if the length of the name is greater than 6
        if len(name) > 6:
            # Check if the first character and the last character of the name are the same
            if name[0] == name[-1]:
                result.append(name)
    return result