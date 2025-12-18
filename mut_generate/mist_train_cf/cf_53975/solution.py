"""
QUESTION:
Create a function `longest_names_lengths(names)` that takes a list of names as input and returns two values: a list of the lengths of each name in the input list, and a string describing the longest name(s) along with its length. If there are multiple names with the maximum length, include all of them in the output string. The function should handle the case where the input list is empty.
"""

def longest_names_lengths(names):
    if not names:    
        return [], "The list is empty."
    
    lengths = [len(name) for name in names]
    max_length = max(lengths)
    longest_names = [name for name in names if len(name) == max_length]
    
    if len(longest_names) > 1:
        result = "The longest names are " + ", ".join(longest_names) + " with a length of " + str(max_length) + "."
    else:
        result = "The longest name is " + longest_names[0] + " with a length of " + str(max_length) + "."
    
    return lengths, result