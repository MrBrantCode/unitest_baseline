"""
QUESTION:
Create a function `sum_of_prime_palindrome(numbers)` that takes a list of integers as input and returns a tuple containing the sum of all prime numbers in the list and a boolean indicating whether the sum is a palindrome.
"""

def sum_of_prime_palindrome(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    primes = [x for x in numbers if is_prime(x)]
    prime_sum = sum(primes)
    return prime_sum, is_palindrome(prime_sum)