"""
QUESTION:
Create a function `sumToN` that takes an integer `n` (1 ≤ n ≤ 10^3) as input and returns the sum of a custom Fibonacci series from 1 to `n`. The custom Fibonacci series starts with 1 and 3, and each subsequent number is the sum of the previous two.
"""

def sumToN(n: int) -> int:
    """
    Calculate the sum of a custom Fibonacci series from 1 to n.
    
    The custom Fibonacci series starts with 1 and 3, and each subsequent number 
    is the sum of the previous two.

    Args:
        n (int): An integer (1 ≤ n ≤ 10^3) specifying the number of terms.

    Returns:
        int: The sum of the custom Fibonacci series up to n terms.
    """
    fibonacci = [1, 3]
    total_sum = 0

    for i in range(n):
        total_sum += fibonacci[i % 2]
        if i > 0:
            fibonacci[i % 2] = fibonacci[0] + fibonacci[1]

    return total_sum