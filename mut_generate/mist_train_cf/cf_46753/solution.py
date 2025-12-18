"""
QUESTION:
Write a function called `sort_strings` that takes two arrays of strings, merges them, removes any duplicates, and sorts the merged result in reverse lexicographical order. The function should exclude strings containing numerical or special characters, only including strings composed solely of alphabetic characters.
"""

import re

def sort_strings(arr1, arr2):
    merged_array = arr1 + arr2
    clean_array = []
    pattern = re.compile('^[a-zA-Z]+$')
    for string in merged_array:
        if pattern.match(string):
            clean_array.append(string)
    unique_array = list(set(clean_array))
    unique_array.sort(reverse=True)
    return unique_array