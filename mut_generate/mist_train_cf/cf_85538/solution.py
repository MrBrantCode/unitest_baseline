"""
QUESTION:
Create a function named `create_dicts(n)` that generates a list of `n` dictionaries. Each dictionary should have a unique string key in the format "dict_i" and its corresponding value should be another dictionary with a unique string key in the format "nested_key_i" and an integer value `i`.
"""

def create_dicts(n):
    return [{f"dict_{i}": {f"nested_key_{i}": i}} for i in range(1, n+1)]