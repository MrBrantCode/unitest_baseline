"""
QUESTION:
Create a function `merge_remove_duplicates_sort` that takes two lists `a` and `b` as input, merges them into one list, removes any duplicate values, and returns the resulting list in ascending order without using built-in sort functions.
"""

def merge_remove_duplicates_sort(a, b):
    c = a + b  # merge two arrays
    unique_c = list(set(c))  # remove duplicates
    sorted_c = []
    while unique_c:  # while unique_c is not empty
        min_value = unique_c[0]
        for x in unique_c:  # find minimum value in the list
            if x < min_value:
                min_value = x
        sorted_c.append(min_value)
        unique_c.remove(min_value)  # remove that minimum value from the list
    return sorted_c