"""
QUESTION:
Write a function `prime_generator` that generates a continuous sequence of prime numbers with a given starting number and gap between consecutive primes. The function should utilize recursion and a generator to produce the prime numbers. The function should take two parameters: `starting_number` and `step`. The function should yield the prime numbers for which `(count % step == 0)`, where `count` is the number of prime numbers generated. The function should use a helper function to check if a number is prime.
"""

def prime_generator(starting_number, step):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0  # Keep track of generated prime numbers
    while True:
        if is_prime(starting_number):
            if count % step == 0:  # Only yield the prime numbers for which (count % step == 0)
                yield starting_number
            count += 1  # increase count for each prime number generated
        starting_number += 1