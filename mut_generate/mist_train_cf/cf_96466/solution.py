"""
QUESTION:
Create a recursive function called `sum_of_primes` that takes two parameters: `num` and `count`. The function should return the sum of the first 15 prime numbers, with `num` being the current number being checked for primality and `count` keeping track of how many prime numbers have been found so far. The function should return the sum as a sequence of prime numbers in reverse order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(num, count, prime_sum=0, prime_list=None):
    if prime_list is None:
        prime_list = []
    if is_prime(num):
        count += 1
        prime_list.append(num)
    if count == 15:
        return prime_list
    if count < 15:
        return sum_of_primes(num + 1, count, prime_sum, prime_list)