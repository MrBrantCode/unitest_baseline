"""
QUESTION:
Write a function named `find_singular_elements` that takes three arrays `l1`, `l2`, and `l3` as input. The function should return an array of elements that are present at the same index in all three arrays and appear only once in each array, up to the length of the shortest array. The function should be able to handle arrays of different lengths and elements of different data types, including integers, strings, and floating point numbers.
"""

def find_singular_elements(l1, l2, l3):
    singular_elements = []
    min_len = min(len(l1), len(l2), len(l3))

    for i in range(min_len):
        if l1[i] == l2[i] == l3[i] and l1.count(l1[i]) == 1 and l2.count(l2[i]) == 1 and l3.count(l3[i]) == 1:
            singular_elements.append(l1[i])

    return singular_elements