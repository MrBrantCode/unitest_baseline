"""
QUESTION:
Write a function to calculate the computational complexity of an algorithm given its input size. The function name should be `calculate_complexity`.
"""

def calculate_complexity(n):
    """
    Calculate the computational complexity of an algorithm given its input size.

    Args:
        n (int): The size of the input data.

    Returns:
        str: A string describing the computational complexity.
    """
    if n == 1:
        return "O(1) - Constant time complexity"
    elif n == 0:
        return "O(log n) - Logarithmic time complexity"
    else:
        return f"O(n^{n}) - Polynomial time complexity"