"""
QUESTION:
Create a function `generate_prime_numbers(n)` to generate a list of consecutive prime numbers starting from 2 up to a given number `n`, where `n` is an integer greater than 2. The function should return a list of prime numbers.
"""

def generate_prime_numbers(n):
    prime_numbers = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers