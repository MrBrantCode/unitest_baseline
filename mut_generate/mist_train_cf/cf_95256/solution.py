"""
QUESTION:
Implement a function `find_kth_largest_prime(arr, k)` that finds the kth largest prime number in the given array. The function should have a time complexity of O(n) or better and should not use any built-in sorting functions or data structures, external libraries, or modules. The function should not modify the original array and should be memory efficient, using no additional space proportional to the size of the input array.
"""

import math

def find_kth_largest_prime(arr, k):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in arr if is_prime(num)]
    primes.sort(reverse=True)
    return primes[k-1] if k <= len(primes) else None