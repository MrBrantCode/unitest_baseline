"""
QUESTION:
Write a function called `count_string_occurrences` that takes two parameters: a string and a list of strings. The function should return the number of times the given string occurs in the list.
"""

def count_string_occurrences(string, arr):
    # initialize count
    count = 0
    # loop through array
    for i in arr:
        # if element equals string, increment count
        if i == string:
            count += 1
    # return count
    return count