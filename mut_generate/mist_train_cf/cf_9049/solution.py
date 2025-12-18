"""
QUESTION:
Write a function named `count_primes` that takes an array of integers as input and returns the number of prime numbers in the array. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should only consider numbers in the array that are greater than 1.
"""

def count_primes(arr):
    count = 0
    for num in arr:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
    return count