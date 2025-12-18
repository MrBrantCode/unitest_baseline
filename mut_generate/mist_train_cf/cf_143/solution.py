"""
QUESTION:
Reorder a given array in a specialized order, maintaining the relative order of prime and non-prime numbers, and implement the reordering algorithm with a time complexity of O(n), where n is the size of the input array. Implement the solution in a function called `reorder_specialized(arr)`.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def reorder_specialized(arr):
    primes = []
    nonPrimes = []

    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            nonPrimes.append(num)

    result = primes + nonPrimes
    return result