"""
QUESTION:
Create a function named filtered_sum that takes a list of integers as input and returns the sum of all integers in the list that meet the following conditions: the integer is divisible by 6, the integer is a prime number, and the sum of the digits of the integer is greater than 10.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def filtered_sum(nums):
    """
    Returns the sum of all integers in the list that are divisible by 6, 
    prime, and have a digit sum greater than 10.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The sum of the filtered integers.
    """
    return sum(num for num in nums if num % 6 == 0 and is_prime(num) and digit_sum(num) > 10)