"""
QUESTION:
Create a function named `vector_check` that takes two distinct numeric vectors as input and returns a boolean value. The function should return `True` if any component from the first vector exists in the second one and `False` otherwise.
"""

def vector_check(vector1, vector2):
    for i in vector1:
        if i in vector2:
            return True
    return False