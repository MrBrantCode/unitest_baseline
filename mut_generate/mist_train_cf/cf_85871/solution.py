"""
QUESTION:
Create a function `filter_strings` that takes a list of strings and an integer `n` as input. Return a list of tuples where each tuple contains a string from the original list that is longer than `n` characters and its corresponding index in the original list.
"""

def filter_strings(lst, n):
    new_list = []
    for i, string in enumerate(lst):
        if len(string) > n:
            new_list.append((string, i))
    return new_list