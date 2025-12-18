"""
QUESTION:
Write a function `count_unique_pairs` that takes a dictionary as input and returns the number of unique key-value pairs without using the built-in `len()` function. The function should have a time complexity of O(n), where n is the number of key-value pairs in the dictionary.
"""

def count_unique_pairs(dictionary):
    count = 0
    seen_pairs = set()

    for key, value in dictionary.items():
        pair = (key, value)
        if pair not in seen_pairs:
            seen_pairs.add(pair)
            count += 1

    return count