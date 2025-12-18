"""
QUESTION:
Write a function `findPermutations(s)` that generates all unique permutations of a given alphanumeric string `s` while considering case sensitivity. The function should handle invalid inputs by returning an error message if `s` contains non-alphanumeric characters or is an empty string.
"""

from itertools import permutations

def findPermutations(s): 
    # check for invalid input
    if not s.isalnum() or s == '':
        return "Invalid input. Please use alphanumeric characters only."
    
    # create a set to automatically remove duplicate permutations
    permSet = set([''.join(p) for p in permutations(s)]) 

    return list(permSet)