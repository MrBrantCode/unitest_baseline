"""
QUESTION:
Reorder a given array in a specialized order while maintaining the relative order of prime and non-prime numbers. Implement the reordering algorithm with a time complexity of O(n). 

The function should be named `reorder_specialized` and take one parameter `arr`, an array of integers. The function should return the reordered array.
"""

def reorder_specialized(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    nonPrimes = []

    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            nonPrimes.append(num)

    result = primes + nonPrimes
    return result