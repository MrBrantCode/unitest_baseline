"""
QUESTION:
Write a function `compare_hashes` that compares two hashes (dictionaries) and returns True if they have the same set of keys and values. The function should have a time complexity of O(n), where n is the number of key-value pairs in the hashes.
"""

def compare_hashes(hash1, hash2):
    if len(hash1) != len(hash2):
        return False

    sorted_keys1 = sorted(hash1.keys())
    sorted_keys2 = sorted(hash2.keys())

    for key1, key2 in zip(sorted_keys1, sorted_keys2):
        if key1 != key2 or hash1[key1] != hash2[key2]:
            return False

    return True