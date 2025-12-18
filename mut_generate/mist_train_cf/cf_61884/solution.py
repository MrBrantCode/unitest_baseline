"""
QUESTION:
Create a function named get_prime_numbers(k, n) that generates a list of all prime numbers between k and n (inclusive). The function should take two parameters, k and n, and return a list of integers.
"""

def get_prime_numbers(k, n):
    prime_numbers = []
    for num in range(k, n + 1):
        if num > 1: # all prime numbers are greater than 1
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0: # condition for non-prime number
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers