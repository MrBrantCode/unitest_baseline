"""
QUESTION:
Write a function `generate_sequence` that calculates the Fibonacci sequence up to the nth term using an iterative approach, and returns the sequence as a list. The function should be able to handle large values of n (up to 10^18) efficiently. It should also have an option to calculate the Fibonacci sequence modulo m, where m is a user-defined input. The function should use constant space complexity, excluding the space needed to store the output sequence.
"""

def generate_sequence(n, m=None):
    """
    Generates the Fibonacci sequence up to the nth term using an iterative approach.

    Args:
        n (int): The number of terms in the Fibonacci sequence.
        m (int, optional): The modulo value. Defaults to None.

    Returns:
        list: The Fibonacci sequence as a list.
    """
    if n <= 0:
        return []

    sequence = [0, 1]
    for i in range(2, n):
        if m is not None:
            sequence.append((sequence[i - 1] + sequence[i - 2]) % m)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence