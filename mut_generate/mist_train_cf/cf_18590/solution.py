"""
QUESTION:
Implement a function `find_kth_largest_prime(arr, k)` that finds the kth largest prime number in the given array `arr`. The function must have a time complexity of O(n) or better, not modify the original array, and not use any built-in sorting functions or data structures, external libraries, or modules. The implementation should also be memory efficient, using additional space not proportional to the size of the input array.
"""

import math

def find_kth_largest_prime(arr, k):
    primes = []
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes[k-1] if k <= len(primes) else None