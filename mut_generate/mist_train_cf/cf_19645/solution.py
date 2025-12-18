"""
QUESTION:
Design a function called `find_prime_numbers` that takes an integer `n` as input and returns a list of prime numbers up to `n`. For each prime number found, the function should also determine and display the sum of its prime factors. The function should not take any other inputs or arguments and should not rely on any external state or variables.
"""

def find_prime_numbers(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_prime_factors(num):
        prime_factors = []
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0 and is_prime(i):
                prime_factors.append(i)
        return sum(prime_factors)

    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
            print("Prime Number:", num)
            print("Sum of Prime Factors:", sum_prime_factors(num))
            print("------------------------")
    return primes