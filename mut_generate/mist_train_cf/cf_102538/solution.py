"""
QUESTION:
Create a function named `calculate_fibonacci_sequence` that uses an iterative method to calculate the Fibonacci sequence up to the nth term. The function should be able to handle large values of n (up to 10^18) efficiently without causing a memory overflow or taking an excessive amount of time to compute. It should also provide options to calculate the sequence modulo m and use constant space complexity.
"""

def calculate_fibonacci_sequence(n, m=None):
    """
    Calculate the Fibonacci sequence up to the nth term.

    Args:
        n (int): The number of terms in the sequence.
        m (int, optional): The modulo value for the sequence. Defaults to None.

    Returns:
        list: The Fibonacci sequence up to the nth term.
    """

    # Handle edge cases
    if n <= 0:
        return []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    # Initialize the sequence with the first two numbers
    sequence = [0, 1]
    a, b = 0, 1

    # Calculate the Fibonacci sequence
    for _ in range(2, n):
        # Calculate the next number in the sequence
        a, b = b, a + b

        # Apply modulo operation if specified
        if m is not None:
            a, b = b % m, (a + b) % m

        # Append the next number to the sequence
        sequence.append(b)

    return sequence