"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed, preserving the original order of elements. The function should not use any built-in or library functions and should optimize for both time and space complexity.
"""

def remove_duplicates(input_list):
    seen = {}
    output = []
    for item in input_list:
        if item not in seen:
            output.append(item)
            seen[item] = 1
    return output