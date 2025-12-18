"""
QUESTION:
Write a function `find_primes(n, k)` that finds all prime numbers between 2 and `n` (inclusive) with a maximum prime number size of `k`. The function should return a dictionary where the keys are the prime numbers and the values are their prime factors in descending order. If a prime number exceeds `k`, exclude it from the results.
"""

def find_primes(n, k):
    def is_prime(num):
        # check for factor other than 1 and num
        for i in range(2,num):
            if(num % i==0):
                return False
        return True

    prime_dict = {}
    for num in range(2, n+1):
        if is_prime(num) and num <= k:
            prime_dict[num] = [1,num]

    return prime_dict