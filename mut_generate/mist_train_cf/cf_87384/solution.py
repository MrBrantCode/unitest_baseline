"""
QUESTION:
Write a function `largest_prime_palindrome` that takes a sequence of integers as input and returns the largest prime palindrome in the sequence. If no prime palindromes are found, return -1. The solution must have a time complexity of O(n), where n is the length of the sequence, and use only constant space.
"""

def largest_prime_palindrome(seq):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    largest_palindrome = -1
    for num in seq:
        if is_prime(num) and is_palindrome(num):
            largest_palindrome = max(largest_palindrome, num)
    return largest_palindrome