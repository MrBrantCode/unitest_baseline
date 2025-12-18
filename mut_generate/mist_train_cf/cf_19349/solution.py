"""
QUESTION:
Write a function `find_kth_prime` that takes an integer `k` as input and returns the k-th prime number. The function should be efficient and optimized to handle large values of `k`. The prime number sequence starts from 2.
"""

def find_kth_prime(k):
    primes = []
    count = 0
    num = 2
    while count < k:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            count += 1
        num += 1
    return primes[-1]