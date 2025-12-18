"""
QUESTION:
Write a function called `extract_last_n_primes` that takes a list of integers and an integer `n` as input, and returns a list of the last `n` unique prime numbers from the input list in descending order. The function should ignore any negative integers and non-prime numbers in the list.
"""

def extract_last_n_primes(lst, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    positive_nums = [x for x in lst if x > 0]
    primes = list(set(filter(is_prime, positive_nums)))
    primes.sort(reverse=True)
    return primes[:n]