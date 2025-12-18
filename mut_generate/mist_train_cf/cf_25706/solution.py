"""
QUESTION:
Create a function named `is_prime` that determines whether a given number `n` is a prime number. The function should return a boolean value. The input `n` is an integer, and there are no restrictions on its value. The function should be optimized to handle large numbers efficiently.
"""

def is_prime(n): 
    """
    A better algorithm for determining if a number is prime 
    :param n: The number to determine whether is prime 
    :return: a boolean if the number is prime
    """
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
  
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
  
    return True