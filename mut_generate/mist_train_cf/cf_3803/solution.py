"""
QUESTION:
Write a function named `get_shortest_string` that takes two strings as arguments and returns the shortest one without using the built-in `len()` function or any other function for calculating string length. If the strings have equal length, return the first string.
"""

def get_shortest_string(str1, str2):
    count1 = 0
    count2 = 0
    for char in str1:
        count1 += 1
    for char in str2:
        count2 += 1

    if count1 < count2:
        return str1
    elif count2 < count1:
        return str2
    else:
        return str1