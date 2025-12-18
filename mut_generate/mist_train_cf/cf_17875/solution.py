"""
QUESTION:
Create a function called `cube_of_primes(n)` that generates a dictionary where the keys are prime numbers up to `n` and their corresponding values are the cube of these prime numbers. The function should also return the total number of prime numbers added to the dictionary.
"""

def cube_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes_dict = {}
    count = 0
    for num in range(2, n+1):
        if is_prime(num):
            primes_dict[num] = num ** 3
            count += 1
    return primes_dict, count