"""
QUESTION:
Write a function named `compare_hashes` that takes two dictionaries as input and returns `True` if they have the same set of keys and values, and `False` otherwise. The function should have a time complexity of O(n), where n is the number of key-value pairs in the dictionaries.
"""

def compare_hashes(hash1, hash2):
    if len(hash1) != len(hash2):
        return False

    for key, value in hash1.items():
        if key not in hash2 or hash2[key] != value:
            return False

    return True