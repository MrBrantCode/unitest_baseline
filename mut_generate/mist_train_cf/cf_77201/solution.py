"""
QUESTION:
Write a function `find_palindrome_and_prime(n)` that returns a list of numbers within the range 1 to `n` (inclusive) that are both prime numbers and palindromes. The function should be able to efficiently handle large values of `n`.
"""

def find_palindrome_and_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    return [i for i in range(1, n+1) if is_prime(i) and is_palindrome(i)]