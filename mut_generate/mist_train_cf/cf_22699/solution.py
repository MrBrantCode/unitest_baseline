"""
QUESTION:
Implement a function `generate_primes` that takes an integer `n` as input and returns a list of the first `n` prime numbers. The function should use an efficient algorithm for prime number generation without utilizing built-in mathematical functions or libraries, relying solely on basic arithmetic operations and logical operators. Additionally, calculate and return the sum of the generated prime numbers.
"""

def generate_primes(n):
    primes = []
    num = 2
    total_sum = 0
    while len(primes) < n:
        if num <= 1:
            is_prime = False
        elif num <= 3:
            is_prime = True
        elif num % 2 == 0 or num % 3 == 0:
            is_prime = False
        else:
            i = 5
            is_prime = True
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6
        if is_prime:
            primes.append(num)
            total_sum += num
        num += 1
    return primes, total_sum