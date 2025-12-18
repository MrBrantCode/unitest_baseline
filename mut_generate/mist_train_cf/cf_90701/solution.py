"""
QUESTION:
Create a function `generate_prime_numbers` that takes an integer `n` as input and returns a list of the first `n` prime numbers. The function should not use any external libraries or functions for prime number generation and have a time complexity of O(n^2) or better.
"""

def generate_prime_numbers(n):
    prime_numbers = []
    num = 2  

    while len(prime_numbers) < n:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

        num += 1

    return prime_numbers