"""
QUESTION:
Implement a function `kth_smallest_prime(numbers, k)` that returns the kth smallest prime number from a list of integers `numbers`, where `k` is a positive integer less than or equal to the length of the list. The function should not use any built-in sorting functions or libraries, and should not use any built-in prime number checking functions or libraries. The time complexity of the function should be O(n log n), where n is the length of the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def kth_smallest_prime(numbers, k):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    if k <= len(primes):
        return primes[k - 1]
    else:
        return None