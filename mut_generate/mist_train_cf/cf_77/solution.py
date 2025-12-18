"""
QUESTION:
Implement a function `sum_of_unique_primes` that calculates the sum of all unique prime numbers in an array. The function should not use any built-in functions or libraries to calculate the sum or determine whether a number is prime. The input array can contain negative numbers and duplicate elements, and the function should not modify the original array. The time complexity of the algorithm should be O(n), where n is the number of elements in the array, and no additional data structures should be used beyond a constant amount of extra memory.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_unique_primes(arr):
    prime_sum = 0
    primes_seen = set()

    for num in arr:
        if num in primes_seen:
            continue

        if is_prime(num):
            prime_sum += num
            primes_seen.add(num)

    return prime_sum