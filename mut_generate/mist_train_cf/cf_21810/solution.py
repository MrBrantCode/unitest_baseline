"""
QUESTION:
Write a function `sort_strings_by_length` that takes a list of strings as input and returns a list of strings sorted in descending order by their lengths without using any built-in sorting functions or libraries.
"""

def sort_strings_by_length(strings):
    n = len(strings)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if len(strings[j]) < len(strings[j+1]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings