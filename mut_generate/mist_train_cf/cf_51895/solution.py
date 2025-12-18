"""
QUESTION:
Develop a Python function `count_numerals` that takes an object as input and returns a dictionary where the keys are the unique numerical characters and the values are their frequencies. The object can be a string, list, tuple, set, or dictionary, and the function should be able to traverse nested data structures and count the numerical characters in the strings contained within them. The function should use a recursive approach and have a time complexity of O(n) and space complexity of O(n).
"""

def count_numerals(obj, counts=None):
    if counts is None:
        counts = dict()

    if isinstance(obj, str):
        for char in obj:
            if char.isdigit():
                counts[char] = counts.get(char, 0) + 1
                
    elif isinstance(obj, dict):
        for key in obj:
            count_numerals(obj[key], counts)

    elif isinstance(obj, (list, tuple, set)):
        for item in obj:
            count_numerals(item, counts)

    return counts