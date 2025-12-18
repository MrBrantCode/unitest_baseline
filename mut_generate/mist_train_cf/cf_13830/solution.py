"""
QUESTION:
Create a function `generate_sequence(k, n)` that takes two parameters: the starting number `k` and the ending number `n`. The function should return a sequence of integers that starts at `k` and ends at `n`, where each integer `i` in the sequence is followed by its square (`i^2`) and its cube (`i^3`).
"""

def generate_sequence(k, n):
    """
    Generates a sequence of integers from k to n, where each integer i is followed by its square (i^2) and its cube (i^3).

    Args:
        k (int): The starting number of the sequence.
        n (int): The ending number of the sequence.

    Returns:
        list: A list of integers representing the sequence.
    """
    sequence = []
    for i in range(k, n+1):
        sequence.extend([i, i**2, i**3])
    return sequence