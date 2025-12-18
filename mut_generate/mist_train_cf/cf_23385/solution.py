"""
QUESTION:
Write a function called `count_prime_num(x, y)` that takes two integers `x` and `y` as input and returns the number of prime numbers between `x` and `y` (inclusive). The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def count_prime_num(x, y):
    """
    This function counts the number of prime numbers between x and y (inclusive).
    
    Parameters:
    x (int): The lower bound of the range (inclusive).
    y (int): The upper bound of the range (inclusive).
    
    Returns:
    int: The number of prime numbers between x and y.
    """
    prime_count = 0
  
    for num in range(x, y + 1): 
       if num > 1: 
           for i in range(2, num): 
               if (num % i) == 0: 
                   break
           else: 
               prime_count += 1
  
    return prime_count