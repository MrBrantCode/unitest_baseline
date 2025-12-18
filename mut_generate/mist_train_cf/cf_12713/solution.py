"""
QUESTION:
Write a function called `non_palindromic_primes` that returns the first 5 non-palindromic prime numbers. A palindromic number reads the same backward as forward. The input should be the count of non-palindromic prime numbers, which is 5 in this case.
"""

def non_palindromic_primes(n):
    """Return the first n non-palindromic prime numbers."""
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        """Check if a number is a palindrome."""
        return str(num) == str(num)[::-1]

    non_palindromic_primes = []
    num = 2
    while len(non_palindromic_primes) < n:
        if is_prime(num) and not is_palindrome(num):
            non_palindromic_primes.append(num)
        num += 1
    return non_palindromic_primes