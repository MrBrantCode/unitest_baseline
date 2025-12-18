"""
QUESTION:
Write a function called findDescendingPrimes that takes an array of integers as input and prints all the prime numbers in descending order. The function should have a time complexity less than O(n^2), where n is the size of the input array.
"""

import heapq
import math

def findDescendingPrimes(arr):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    descending_primes = []
    for num in arr:
        if isPrime(num):
            heapq.heappush(descending_primes, -num)  # Use negative numbers for max heap effect
    while descending_primes:
        print(-heapq.heappop(descending_primes))