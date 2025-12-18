"""
QUESTION:
Write a function called `find_subsets` to generate all possible subsets of a given string. The function should take a string and return all possible subsets of the string, including the empty string. It should not include duplicate subsets and should not use any external libraries or data structures other than strings.
"""

def find_subsets(string, current_subset="", index=0):
    if index == len(string):
        return [current_subset]
    
    subsets = []
    subsets.extend(find_subsets(string, current_subset + string[index], index + 1))
    subsets.extend(find_subsets(string, current_subset, index + 1))
    
    return subsets