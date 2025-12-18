"""
QUESTION:
Write a function `sum_of_squares_of_fibs` that calculates the sum of squares of Fibonacci numbers up to the nth number in the sequence. The function should take one argument `n`, representing the position of the Fibonacci number up to which the sum is to be calculated.
"""

def sum_of_squares_of_fibs(n):
    """
    Calculates the sum of squares of Fibonacci numbers up to the nth number in the sequence.

    Args:
        n (int): The position of the Fibonacci number up to which the sum is to be calculated.

    Returns:
        int: The sum of squares of Fibonacci numbers up to the nth number.
    """
    fib_nums = [0, 1]
    [fib_nums.append(fib_nums[k-1] + fib_nums[k-2]) for k in range(2, n+1)]
    return sum(i**2 for i in fib_nums)