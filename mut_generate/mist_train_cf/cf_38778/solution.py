"""
QUESTION:
Implement the `find_max_path_value(keys)` function, which takes a list of binary keys and returns the maximum integer path value obtained by converting each binary key to an integer using `int.from_bytes(k, 'big')`. The function should handle a list of binary keys where each key is a bytes object, and return an integer representing the maximum path value.
"""

def find_max_path_value(keys):
    return max(int.from_bytes(k, 'big') for k in keys)