"""
QUESTION:
Write a function `merge_and_sort(s1, s2)` that merges two input strings `s1` and `s2` into one string. The function should remove any numbers and special characters from the combined string, convert it to lowercase, remove duplicate characters, and sort the remaining characters in alphabetical order.
"""

def merge_and_sort(s1, s2):
    # Combining two strings
    s = s1 + s2
    
    # Removing numbers and special characters
    s = ''.join([i for i in s if i.isalpha()])

    # Converting string to lowercase and removing duplicates
    s = ''.join(sorted(set(s.lower())))

    return s