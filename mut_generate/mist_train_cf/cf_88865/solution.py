"""
QUESTION:
Write a function `convert_to_dictionary(lst)` that takes a list of strings as input, removes duplicates, and returns a dictionary where the keys are the unique strings and the values are their corresponding lengths. The function should have a time complexity of O(n) and should not use built-in functions or methods for direct list-to-dictionary conversion or duplicate removal. It should also handle edge cases such as an empty input list or a list containing only duplicate strings.
"""

def convert_to_dictionary(lst):
    if len(lst) == 0:
        return {}
    
    unique_lst = []
    lengths = {}
    
    for string in lst:
        if string not in unique_lst:
            unique_lst.append(string)
            lengths[string] = len(string)
    
    return lengths