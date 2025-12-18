"""
QUESTION:
Create a recursive function `recursiveSum` that takes an integer `n` as input, where `n` is between 100 and 1000, and returns the sum of all integers from 1 to `n`. The function should only print the sum if it is a prime number. Estimate the time complexity of this function.
"""

def recursiveSum(n):
    """
    A recursive function that calculates the sum of all integers from 1 to n.
    
    Args:
        n (int): The upper limit of the range.
    
    Returns:
        int: The sum of all integers from 1 to n.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_recursive(i, total):
        if i > n:
            if is_prime(total):
                print(total)
            return total
        return sum_recursive(i + 1, total + i)

    return sum_recursive(1, 0)