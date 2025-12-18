"""
QUESTION:
Design a function named `prime_composite_array` that takes an array as input and returns a dictionary containing the following information:

- The length of the array
- A boolean indicating whether the length of the array is prime
- A list of prime numbers up to the length of the array
- A list of composite numbers up to the length of the array
- A list of factors of the length of the array if it is composite, otherwise a message indicating that the length is a prime number

The function should be efficient and accurate.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_composite_array(arr):
    length = len(arr)
    prime, composite = [], []
    for i in range(2, length+1):
        if is_prime(i):
            prime.append(i)
        else:
            composite.append(i)
            
    factors = [i for i in range(1, length + 1) if length % i == 0]

    return {
        "length": length,
        "is_prime": is_prime(length),
        "primes": prime,
        "composites": composite,
        "factors": factors 
        if not is_prime(length) else "No factors as length is a prime number"
    }