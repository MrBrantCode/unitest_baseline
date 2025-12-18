"""
QUESTION:
Create a function called `highest_prime_palindrome` that takes a list of integers as input and returns the highest prime number that is also a palindrome in the list. If no such number exists, return `None`. The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself, and a palindrome as a number or a text phrase that reads the same backwards as forwards.
"""

def highest_prime_palindrome(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    prime_palindromes = [num for num in nums if is_prime(num) and is_palindrome(num)]
    return max(prime_palindromes) if prime_palindromes else None