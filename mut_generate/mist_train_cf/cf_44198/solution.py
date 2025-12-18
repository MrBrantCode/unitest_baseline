"""
QUESTION:
Find a function `find_prime_numbers` that takes one or more lists of integers as input, filters out non-prime numbers, and returns a list of tuples. Each tuple contains three elements: a sorted list of prime numbers in ascending order, the product of all prime numbers, and the sum of all prime numbers. The function should handle exceptions for non-numerical inputs, floating point numbers, and large numbers that surpass the maximum integer limit in Python, without triggering a memory overflow.
"""

import functools
    
def compute_product(x, y):
    return str(int(x) * int(y))

def find_prime_numbers(*input_lists):
    output = []
    for input_list in input_lists:
        primes = []
        input_list = [i for i in input_list if type(i) == int and i > 1]
        if input_list:
            n = max(input_list)+1
            sieve = [True] * (n//2)
            for i in range(3,int(n**0.5)+1,2):
                if sieve[i//2]:
                    sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
            primes = [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
            primes = sorted([num for num in primes if num in input_list])
        prime_product = functools.reduce(compute_product, primes, '1')
        prime_sum = sum(map(int, primes))
        output.append((primes, int(prime_product), prime_sum))
    return output