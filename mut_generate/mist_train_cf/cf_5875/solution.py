"""
QUESTION:
Write a function called `is_perfect_prime` that checks whether a given positive integer is a perfect prime or not. A perfect prime is a prime number that is also equal to the sum of all its divisors, including 1 and itself. The function should use a helper function called `get_divisors` to find all the divisors of a given number, which should return a list of all the divisors. 

The `get_divisors` function should have a time complexity of O(n), where n is the input number. The function should not use any external libraries or pre-defined functions to find the divisors.
"""

def get_divisors(n):
    """Returns a list of all the divisors of a given number n."""
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_prime(n):
    """Checks whether a given positive integer is a perfect prime or not."""
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    divisors = get_divisors(n)
    divisor_sum = sum(divisors)

    if divisor_sum == n:
        return True
    else:
        return False