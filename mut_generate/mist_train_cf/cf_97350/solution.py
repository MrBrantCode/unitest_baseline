"""
QUESTION:
Given a list of strings and an input string, write a function named `find_last_occurrence` that returns the index of the last occurrence of the input string in the list. The search should be case-sensitive. If the input string does not exist in the list, the function should return -1.
"""

def find_last_occurrence(lst, string):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == string:
            return i
    return -1  # Return -1 if the string is not found in the list