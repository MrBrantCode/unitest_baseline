"""
QUESTION:
Create a function named `find_prime_factors(number)` that takes an integer as input, finds its prime factors, and returns them in a list. The function should be efficient enough to handle large inputs, but there is no specific limit for the input size. The list of prime factors should be in ascending order.
"""

def find_prime_factors(number):
    prime_factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1
    return sorted(prime_factors)