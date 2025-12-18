"""
QUESTION:
Create a function `largest_prime_factor(n: int)` that takes an integer `n` as input, where `abs(n) > 1` and `n` is not a prime number. The function should return the largest prime factor of `n`. The input `n` can be positive or negative, but the output should be the same for both positive and negative inputs. The function should optimize the process by only checking odd factors after 2.
"""

def largest_prime_factor(n: int) -> int:
    """
    This function takes an integer n as input, where abs(n) > 1 and n is not a prime number.
    It returns the largest prime factor of n.
    
    :param n: The input number
    :return: The largest prime factor of n
    """
    n = abs(n)
    divisor = 2
  
    while n % divisor == 0:
        n //= divisor

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor:
            divisor += 2
        else:
            n //= divisor

    return n if n > 2 else divisor