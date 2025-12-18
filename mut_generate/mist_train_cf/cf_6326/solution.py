"""
QUESTION:
Implement a function `filtered_sum` that takes a list of integers as input and returns the sum of all integers that are divisible by 6, are prime numbers, and have a digit sum greater than 10.
"""

def filtered_sum(nums):
    """
    This function calculates the sum of all integers in the input list that are 
    divisible by 6, are prime numbers, and have a digit sum greater than 10.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The sum of all integers that meet the specified conditions.
    """

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n):
        """Calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))

    return sum(num for num in nums if num % 6 == 0 and is_prime(num) and digit_sum(num) > 10)