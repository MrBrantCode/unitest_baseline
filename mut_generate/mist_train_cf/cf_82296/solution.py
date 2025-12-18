"""
QUESTION:
Create a function `unique_elements(array)` that takes an array containing both numbers and strings as input. The function should return a list of all elements that appear only once in the array, sorted in increasing order for numbers and alphabetically for strings. Lowercase and uppercase alphabets are treated as different entities.
"""

def unique_elements(array):
    counts = {}
    for elem in array:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    unique = [elem for elem, count in counts.items() if count == 1]

    return sorted([x for x in unique if isinstance(x, (int, float))]) + sorted([x for x in unique if isinstance(x, str)])