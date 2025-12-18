"""
QUESTION:
Create a function named `string_sequence(n)` that takes an integer `n` as input and returns a string composed of numbers from 0 to `n`, all separated by a space.
"""

def string_sequence(n):
    """Return a string composed of numbers from 0 to n, all separated by a space."""
    return ' '.join(str(i) for i in range(n + 1))