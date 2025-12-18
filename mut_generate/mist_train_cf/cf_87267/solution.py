"""
QUESTION:
Create a function named `get_prime_numbers` that takes no arguments and returns a list of prime numbers between -50 and 50 in reverse order. The function should include negative numbers in its consideration, as in mathematics, a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers():
    prime_numbers = [num for num in range(-50, 51) if is_prime(abs(num)) and abs(num) > 1]
    prime_numbers.sort(key=abs, reverse=True)
    return prime_numbers