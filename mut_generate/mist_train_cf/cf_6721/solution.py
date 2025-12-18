"""
QUESTION:
Write a function called `find_max_length_strings` that takes a list of strings as input. The function should return a list of all strings that have the maximum length in the input list. If there are multiple strings with the maximum length, return all of them. If the input list is empty, return an empty list.
"""

def find_max_length_strings(lst):
    if len(lst) == 0:
        return []
    
    max_length = len(max(lst, key=len))
    max_length_strings = [string for string in lst if len(string) == max_length]
    
    return max_length_strings