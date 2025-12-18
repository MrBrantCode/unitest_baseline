"""
QUESTION:
Implement a function `sieve_of_eratosthenes(lower, upper)` that generates a sequence of prime numbers between a given range using the Sieve of Eratosthenes algorithm. The function should take two parameters, `lower` and `upper`, which define the range of numbers to check for primality, and return a list of prime numbers within this range.
"""

def sieve_of_eratosthenes(lower, upper):
    prime_list = [True] * (upper + 1)
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2, int(upper ** 0.5) + 1):
        if prime_list[i]:
            for j in range(i*i, upper + 1, i):
                prime_list[j] = False

    prime_nums = []
    for i in range(lower, upper + 1):
        if prime_list[i]:
            prime_nums.append(i)

    return prime_nums