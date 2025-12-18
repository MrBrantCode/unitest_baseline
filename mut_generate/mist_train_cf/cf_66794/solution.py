"""
QUESTION:
Write a function `sum_of_integers` that takes an array of mixed elements as input, which may contain integers, strings, or nested arrays. The function should recursively traverse the array and its nested arrays, ignoring non-integer elements, and return the sum of all integer elements.
"""

def sum_of_integers(arr):
    total = 0
    for a in arr:
        if type(a) == int:
            total += a
        elif type(a) == list:
            total += sum_of_integers(a)
    return total