"""
QUESTION:
Create a function `create_indexed_dict` that takes a list of unique strings as input and returns a dictionary where each string in the list is a key and its corresponding value is its index in the list.
"""

def create_indexed_dict(lst):
    """Create a dictionary where each string in the list is a key and its corresponding value is its index in the list."""
    return {k: v for v, k in enumerate(lst)}