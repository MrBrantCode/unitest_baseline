"""
QUESTION:
Write a function `increment_counter` that increments a given integer counter by 20 without using the addition operator (+), multiplication operator (*), or any bitwise operations, and ensuring the time complexity of the solution is O(1).
"""

def increment_counter(counter):
    """Increments the given counter by 20 without using addition, multiplication, or bitwise operations."""
    return counter - (-20)