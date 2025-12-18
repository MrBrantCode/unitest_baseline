"""
QUESTION:
Write a function called `generate_subsets` that takes a string of unique characters as input and returns all possible subsets of the input string. Each subset should be returned as a string and the subsets should be returned in a list. The order of the characters in the original string should be preserved in the subsets. The function should not return any duplicate subsets.
"""

def generate_subsets(s):
    if len(s) == 0:
        return ['']
    
    subsets = []
    first_char = s[0]
    rest_of_string = s[1:]
    
    for subset in generate_subsets(rest_of_string):
        subsets.append(subset)
        subsets.append(first_char + subset)
    
    return subsets