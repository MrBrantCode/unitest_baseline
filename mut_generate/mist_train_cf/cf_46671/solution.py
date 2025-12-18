"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input. The function should return a tuple containing a boolean indicating whether the number is prime and a list of its divisors if it is not prime. The function should be optimized to only check for divisors up to the square root of the input number.
"""

def is_prime(n):
    """ Returns True if a given number is prime, False if not.
    If the number is not prime, return also a list of its divisors.
    """
    if n < 2:
        return False, []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors = [i]
            if i != n // i:
                divisors.append(n // i)
            for j in range(i+1, n // i):
                if n % j == 0:
                    divisors.append(j)
                    if j != n // j:
                        divisors.append(n // j)
            return False, sorted(divisors)
    return True, []