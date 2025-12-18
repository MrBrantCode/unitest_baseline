"""
QUESTION:
Write a function `find_kth_largest_prime(arr, k)` that takes an array `arr` of integers and an integer `k` as input, and returns the kth largest prime number in the array. The function should not modify the original array and should not use any built-in sorting functions or data structures, external libraries or modules, or prime number checking functions or data structures. The function should have a time complexity of O(n) or better and should use minimal extra space. If the kth largest prime number does not exist in the array, the function should return `None`.
"""

def find_kth_largest_prime(arr, k):
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    max_value = max(arr)
    primes = sieve_of_eratosthenes(max_value)

    count = 0
    for num in arr:
        if num in primes:
            count += 1
            if count == k:
                return num

    return None