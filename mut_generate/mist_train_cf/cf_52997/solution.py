"""
QUESTION:
Calculate the sum of the number of terms in the Zeckendorf representation of all positive integers in the range 0 < n < 10^17. 

The function name should be zeckendorf_sum and it should take an upper limit as the input parameter. The function should return the sum of the number of terms in the Zeckendorf representation of all positive integers up to the given upper limit.
"""

def zeckendorf_sum(upper_limit):
    """
    Calculate the sum of the number of terms in the Zeckendorf representation of all positive integers up to the given upper limit.

    Args:
        upper_limit (int): The upper limit of the range.

    Returns:
        int: The sum of the number of terms in the Zeckendorf representation.
    """
    fib = [1, 2]  # Initialize the Fibonacci sequence
    # Generate the Fibonacci sequence up to upper_limit
    while fib[-1] + fib[-2] < upper_limit:
        fib.append(fib[-1] + fib[-2])

    sum_z = 0  # Initialize the sum
    # Calculate the sum
    for i in range(1, len(fib)):
        sum_z += (fib[i] - fib[i-1]) * i
    return sum_z