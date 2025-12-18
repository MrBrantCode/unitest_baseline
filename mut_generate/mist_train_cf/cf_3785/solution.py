"""
QUESTION:
Implement a function `find_kth_largest_prime(arr, k)` that finds the kth largest prime number in the given array `arr`. 

The function should not use any built-in sorting functions or data structures, external libraries or modules, or any prime number checking functions or data structures. It should also not modify the original array and should be memory efficient, not using additional space proportional to the size of the input array. 

The function should return the kth largest prime number if it exists, otherwise return None.
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

        primes = []
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
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