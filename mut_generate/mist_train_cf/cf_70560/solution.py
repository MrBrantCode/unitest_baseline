"""
QUESTION:
Write a function `rotate_array_elements(arr)` that takes an array of integers as input and returns `True` if it's possible to arrange the array in ascending order by rotating the array up to two times, with the following conditions:

- The rotated array contains an odd number of elements less than the average.
- All the prime numbers in the array are at the odd-indexed positions (0-based).
- The function should return `True` if the array is empty.

The input array can contain repeated elements and does not include 0 or negative integers. The function should be efficient and not rely on brute force.
"""

def rotate_array_elements(arr):
    if not arr: return True

    arr_sum = sum(arr)
    arr_len = len(arr)
    arr_avg = arr_sum / arr_len

    def calculate_primes(n):
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n+1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n) if is_prime[p]]

    primes = calculate_primes(max(arr) + 1)
    prime_counter = 0

    rotations = 0
    while rotations < 2:
        odds_less_avg = sum(1 for i, x in enumerate(arr) if i%2 != 0 and x < arr_avg)
        if odds_less_avg%2 == 0: return False

        for i, x in enumerate(arr): 
            if i%2 == 0 and x in primes: 
                if prime_counter < len(primes):
                    arr[i], arr[prime_counter] = arr[prime_counter], arr[i]
                    prime_counter += 1
                else:
                    return False
        rotations += 1

        if sorted(arr) == arr:
            return True

    return False