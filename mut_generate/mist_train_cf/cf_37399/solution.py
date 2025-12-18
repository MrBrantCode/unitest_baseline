"""
QUESTION:
Create a `PrimePalindrome` class with a method `find_largest_prime_palindrome` that takes an integer `n` as input and returns the largest prime palindrome number less than or equal to `n`. A prime number is a positive integer greater than 1 with no divisors other than 1 and itself. A palindrome is a number that reads the same forwards and backwards. If no prime palindrome numbers exist less than or equal to `n`, return 0. The implementation should handle large values of `n` efficiently.
"""

def largest_prime_palindrome(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    for num in range(n, 1, -1):
        if is_prime(num) and is_palindrome(num):
            return num
    return 0