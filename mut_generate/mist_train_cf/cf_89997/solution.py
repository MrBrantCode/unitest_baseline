"""
QUESTION:
Create a function `sort_strings` that takes a list of strings as input, removes duplicates, sorts the strings by their lengths in descending order, and breaks ties alphabetically. The function should have a time complexity of O(n log n) and a space complexity of constant.
"""

def sort_strings(strings):
    # Remove duplicates from the list
    strings = list(set(strings))
    
    # Create a list of tuples with string length and string itself
    tuples = [(len(s), s) for s in strings]
    
    # Sort the list of tuples by length and alphabetically
    tuples.sort(key=lambda x: (-x[0], x[1]))
    
    # Return the sorted strings
    return [t[1] for t in tuples]