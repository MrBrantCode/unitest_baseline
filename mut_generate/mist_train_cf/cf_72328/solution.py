"""
QUESTION:
Write a function `find_prime_palindromes(limit)` that returns a list of prime numbers that are also palindromes and are less than or equal to the given limit. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A palindrome is a number that reads the same backward as forward.
"""

def find_prime_palindromes(limit):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n%i == 0 or n%(i + 2) == 0:
                return False
            i = i + 6
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    prime_palindromes = []
    for num in range(limit+1):
        if is_prime(num) and is_palindrome(num):
            prime_palindromes.append(num)
    return prime_palindromes