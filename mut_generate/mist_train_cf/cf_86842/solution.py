"""
QUESTION:
Construct a function `removePrimes` that takes an array of integers as input, prints the prime numbers in the array in ascending order, and then removes those prime numbers from the array. The time complexity of the function should be O(n * sqrt(max)) where n is the size of the array and max is the maximum number in the array, and the space complexity should be O(1), excluding the space needed for the input and output.
"""

import math

def removePrimes(arr):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    i = 0
    while i < len(arr):
        if isPrime(arr[i]):
            primes.append(arr[i])
            arr.pop(i)
        else:
            i += 1

    primes.sort()
    for prime in primes:
        print(prime)

    return arr