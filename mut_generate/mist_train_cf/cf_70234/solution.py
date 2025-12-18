"""
QUESTION:
Write a function `rotate_array_elements` that takes a list `arr` as input and returns `True` if it's possible to sort the list by rotating its elements at even indices to the positions of prime numbers in the list, and rotating the prime numbers to the positions of the rotated elements. The rotation should be done only twice. The function should also check if the sum of elements at odd indices is even before each rotation. If it's not possible to sort the list, the function should return `False`. The function should use a helper function `calculate_primes` to generate a list of prime numbers up to the maximum element in the input list.
"""

def calculate_primes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n) if is_prime[p]]

def rotate_array_elements(arr):
    if not arr: return True

    arr_sum = sum(arr)
    arr_len = len(arr)
    arr_avg = arr_sum / arr_len

    primes = calculate_primes(max(arr))
    primes_counter = 0
    rotations = 0
    while rotations < 2:
        odds_less_avg = sum(1 for i, x in enumerate(arr) if i % 2 != 0 and x < arr_avg)
        if odds_less_avg % 2 == 0: return False
        
        for i, x in enumerate(arr):
            if i % 2 == 0 and x in primes:
                if primes_counter < len(primes):
                    arr[i], arr[primes_counter] = arr[primes_counter], arr[i]
                    primes_counter += 1
                else:
                    return False
            rotations += 1

        if sorted(arr) == arr:
            return True
    
    return False