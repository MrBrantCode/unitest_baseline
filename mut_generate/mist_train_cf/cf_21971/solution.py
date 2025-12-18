"""
QUESTION:
Create a function called `generate_palindrome_primes_dictionary` that returns a dictionary with 10 elements, where each key is a string representing a palindrome number and the corresponding value is a list of the first 10 prime numbers. The function should not take any arguments.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_palindrome_primes_dictionary():
    palindrome_primes = {}
    count = 0
    number = 2

    while count < 10:
        if str(number) == str(number)[::-1] and is_prime(number):
            palindrome_primes[str(number)] = []
            count += 1
        number += 1

    for key in palindrome_primes.keys():
        primes = []
        i = 2
        while len(primes) < 10:
            if is_prime(i):
                primes.append(i)
            i += 1
        palindrome_primes[key] = primes

    return palindrome_primes