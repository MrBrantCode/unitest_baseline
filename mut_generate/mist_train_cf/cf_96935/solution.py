"""
QUESTION:
Write a function named `check_prime_and_factors` that takes an integer `number` as input and returns a tuple containing a boolean value indicating whether the number is prime or not, and a list of tuples representing the prime factors of the number along with their multiplicities. If the number is prime, the function should return an empty list as the second element of the tuple.
"""

def check_prime_and_factors(number):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors(n):
        factors = []
        i = 2
        while i <= n:
            if n % i == 0:
                count = 0
                while n % i == 0:
                    count += 1
                    n //= i
                factors.append((i, count))
            i += 1
        return factors

    if is_prime(number):
        return True, []
    else:
        return False, prime_factors(number)