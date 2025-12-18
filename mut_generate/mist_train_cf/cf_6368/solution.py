"""
QUESTION:
Given a list of positive integers, create a function called `odd_prime_powers` that returns a new list containing the squares of each odd prime number in the input list. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def odd_prime_powers(nums):
    """
    Returns a new list containing the squares of each odd prime number in the input list.
    
    Args:
        nums (list): A list of positive integers.
    
    Returns:
        list: A list of squares of odd prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [i ** 2 for i in nums if is_prime(i) and i % 2 != 0]