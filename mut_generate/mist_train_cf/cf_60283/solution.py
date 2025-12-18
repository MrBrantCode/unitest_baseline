"""
QUESTION:
Create a function `check_prime_palindrome` that takes four parameters: `n`, `p`, `q`, and `r`. The function should return a list of prime numbers that have `n` digits, are within the range `[p, q]`, are palindromes, are divisible by `r`, and are not divisible by any even number. The function should ignore prime palindromes that are divisible by both `r` and an even number.
"""

def check_prime_palindrome(n, p, q, r):
    """
    This function returns a list of prime numbers that have n digits, are within the range [p, q],
    are palindromes, are divisible by r, and are not divisible by any even number.

    Parameters:
    n (int): Number of digits in prime numbers.
    p (int): Lower bound of the range (inclusive).
    q (int): Upper bound of the range (inclusive).
    r (int): Number to check for divisibility.

    Returns:
    list: A list of prime numbers satisfying the conditions.
    """
    def primes_sieve(limit):
        limitn = limit+1
        primes = dict()
        for ind, val in enumerate([True] * limitn): primes[ind] = val
        primes[0] = primes[1] = False
        for ind, val in enumerate(primes):
            if val is True:
                primes[ind*2::ind] = [False] * (((limit - ind)//ind) - 1)
        return [ind for ind, val in enumerate(primes) if val is True]

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_even(n):
        return n % 2 == 0

    prime_list = [i for i in primes_sieve(q) if i >= p and len(str(i)) == n]
    result = [prime for prime in prime_list if is_palindrome(prime) and prime % r == 0 and not is_even(prime)]
    return result