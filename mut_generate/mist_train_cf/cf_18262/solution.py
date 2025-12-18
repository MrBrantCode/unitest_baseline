"""
QUESTION:
Write a function `compare_hashes(hash1, hash2)` that compares two hashes and returns `True` if they have the same set of keys and values, and `False` otherwise. The function should have a time complexity of O(n), where n is the number of key-value pairs in the hashes.
"""

def compare_hashes(hash1, hash2):
    if len(hash1) != len(hash2):
        return False
    
    for key in hash1:
        if key not in hash2:
            return False
        
        if hash1[key] != hash2[key]:
            return False
    
    return True