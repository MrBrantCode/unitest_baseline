"""
QUESTION:
Design a function `separate_prime_composite` that separates prime numbers and composite numbers from a given list of integers. The function should handle non-integer inputs and optimize performance for large inputs up to 1e6. The function should return three lists: prime numbers, composite numbers, and non-integer inputs.
"""

def separate_prime_composite(num_list):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**.5) + 1, 2))

    primes = []
    composites = []
    invalid_inputs = []

    for num in num_list:
        try:
            if is_prime(num):
                primes.append(num)
            else:
                composites.append(num)
        except TypeError:
            invalid_inputs.append(num)

    return primes, composites, invalid_inputs