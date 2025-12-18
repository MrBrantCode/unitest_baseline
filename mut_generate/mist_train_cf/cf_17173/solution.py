"""
QUESTION:
Write a function `largest_prime_palindrome` that takes a sequence of integers as input and returns the largest prime palindrome in the sequence. If no prime palindrome exists, return -1. The function should have a time complexity of O(n) and use constant space.
"""

def largest_prime_palindrome(seq):
    def is_palindrome(n):
        n_str = str(n)
        return n_str == n_str[::-1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_palindrome = -1
    for n in seq:
        if is_palindrome(n) and is_prime(n):
            largest_palindrome = max(largest_palindrome, n)
    return largest_palindrome