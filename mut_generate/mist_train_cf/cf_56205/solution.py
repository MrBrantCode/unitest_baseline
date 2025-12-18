"""
QUESTION:
Write a function that calculates the number of perfect numbers in the first N numbers of the Lucas sequence. The Lucas sequence is a series of numbers where each number is the sum of the two preceding ones, starting with L(0) = 2 and L(1) = 1. A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. The function should return the count of perfect numbers. The function should be named `count_perfect_lucas_numbers` and it should take an integer `N` as input.
"""

def count_perfect_lucas_numbers(N):
    """
    This function calculates the number of perfect numbers in the first N numbers of the Lucas sequence.

    Args:
        N (int): The number of Lucas sequence numbers to check.

    Returns:
        int: The count of perfect numbers in the first N numbers of the Lucas sequence.
    """
    def is_perfect(n):
        """Check if a number is perfect."""
        sum_divisors = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum_divisors = sum_divisors + i + n//i
                else:
                    sum_divisors = sum_divisors + i
                i += 1
        return sum_divisors == n and n!=1

    def lucas(n):
        """Generate the nth number in the Lucas sequence."""
        a, b = 2, 1
        if n == 0:
            return a
        if n == 1:
            return b
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    count = 0
    for i in range(1, N + 1):
        if is_perfect(lucas(i)):
            count += 1
    return count