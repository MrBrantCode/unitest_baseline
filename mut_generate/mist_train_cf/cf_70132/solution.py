"""
QUESTION:
Create a function called `check_last_element_prime` that takes a deque of integers as input and returns `True` if the last element of the deque is a prime number and `False` otherwise. The function should not use indexing or the `pop` method to access the last element of the deque. The function should also handle non-integer elements in the deque and non-prime numbers.
"""

from collections import deque

def check_last_element_prime(d):
    """
    Check if the last element of the deque is a prime number.
    
    Args:
        d (deque): A deque of integers.
    
    Returns:
        bool: True if the last element is a prime number, False otherwise.
    """
    
    # reverse the deque
    reverse_d = reversed(d)
    
    # get the first element of reversed deque, which is the last element of original deque
    last_element = next(reverse_d)
    
    # check if last element is an integer
    if not isinstance(last_element, int):
        return False
    
    # function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while(i * i <= n):
            if(n % i == 0 or n % (i + 2) == 0):
                return False
            i += 6
        return True
    
    # return True if last element is a prime number
    return is_prime(last_element)