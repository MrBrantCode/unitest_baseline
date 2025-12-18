"""
QUESTION:
Write a function named `unique_elements` that takes three lists (l1, l2, l3) of varying lengths as input and returns a list of unique elements that appear at the same index in all three lists. The function should handle different data types, including integers, strings, and floating point numbers, and only include each unique element once in the output list, up to the length of the shortest input list.
"""

def unique_elements(l1, l2, l3):
    min_len = min(len(l1), len(l2), len(l3))
    unique_elem = []
    for i in range(min_len):
        if l1[i] == l2[i] == l3[i] and l1[i] not in unique_elem:
            unique_elem.append(l1[i])
    return unique_elem