"""
QUESTION:
Write a function `prime_palindrome(limit)` that prints all prime numbers that are also palindromes up to the given limit.
"""

def prime_palindrome(limit):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    for num in range(2, limit + 1):
        if is_prime(num) and is_palindrome(num):
            print(num)