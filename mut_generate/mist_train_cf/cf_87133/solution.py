"""
QUESTION:
Create a function called `prime_palindromes` that prints the first 100 prime numbers that are also palindromes. Each prime number should be checked for divisibility by all prime numbers smaller than it. Use a while loop to find these numbers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def prime_palindromes():
    count = 0
    num = 2
    prime_palindromes = []

    while count < 100:
        if is_prime(num) and is_palindrome(num):
            prime_palindromes.append(num)
            count += 1
        num += 1
    return prime_palindromes