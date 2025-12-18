"""
QUESTION:
Write a function `generate_and_sum_primes` that takes no arguments. The function should generate the first 10 prime numbers between 1000 and 2000, calculate the sum of their digits, and return the prime numbers and the binary representation of the sum of their digits. The function should use a helper function `is_prime` to check if a number is prime, and the prime numbers should be formatted as a table. The binary representation of the sum of digits should be a string without the "0b" prefix.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_and_sum_primes():
    primes = []
    for n in range(1000, 2000):
        if is_prime(n):
            primes.append(n)
            if len(primes) == 10:
                break
    sum_of_digits = sum(int(digit) for prime in primes for digit in str(prime))
    binary_sum = bin(sum_of_digits)[2:]
    return primes, binary_sum