"""
QUESTION:
Write a function named `find_first_occurrence` that takes a list of strings and an input string as parameters. The function should return the index of the first occurrence of the input string in the list. The search should be case-sensitive and return -1 if the input string is not found in the list.
"""

def find_first_occurrence(lst, string):
    for i in range(len(lst)):
        if lst[i] == string:
            return i
    return -1