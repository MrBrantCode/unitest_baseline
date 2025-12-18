"""
QUESTION:
Write a function named `find_non_repeat` that takes a list and an optional comparison function as arguments, and returns the first non-repeating element in the list based on the comparison made through the user-defined equality function. The function should handle edge cases like an empty list or a list where all elements repeat, and should use a hash map for increased efficiency. If no comparison function is provided, it should fall back to a simple equality function.
"""

def find_non_repeat(lst, eq_func=None):
    if eq_func is None: 
        eq_func = lambda x, y: x == y

    frequency_map = {}
    for element in lst: 
        if any(eq_func(element, x) for x in frequency_map):
            frequency_map[next(x for x in frequency_map if eq_func(element, x))] += 1
        else:
            frequency_map[element] = 1

    for element, count in frequency_map.items():
        if count == 1:
            return element

    return None 