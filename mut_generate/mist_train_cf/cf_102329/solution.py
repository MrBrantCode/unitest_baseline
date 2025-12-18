"""
QUESTION:
Create a function called `compact_list` that takes a list of elements as input and returns a new list with all consecutive duplicates removed and all elements at odd positions removed. The input list will always contain at least one element.
"""

def compact_list(my_list):
    result = []
    prev = None
    for i, num in enumerate(my_list):
        if i % 2 == 0 and num != prev:
            result.append(num)
        prev = num
    return result