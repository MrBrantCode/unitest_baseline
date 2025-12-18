"""
QUESTION:
Create a function named `hash_data` that takes a 32-bit integer `data` as input and returns a 32-bit hash value for the given data using only bitwise operators.
"""

def hash_data(data):
    return data ^ (data << 2)