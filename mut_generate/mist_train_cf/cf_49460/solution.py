"""
QUESTION:
Write a function `max_average_subarray` that takes an array of integers and an integer k as input, and returns a tuple containing the maximum average of any subarray of length k that contains at least one prime number and the starting index position of this subarray. The function should return `float('-inf'), -1` if no such subarray exists.
"""

def max_average_subarray(arr, k):
    primes = [False, False] + [True for _ in range(2, max(arr)+1)]
    p = 2
    while p**2 <= max(arr):
        if primes[p]:
            for i in range(p**2, max(arr)+1, p):
                primes[i] = False
        p += 1
    
    n = len(arr)
    max_avg, max_idx = float('-inf'), -1
    
    # Sum of first k elements
    window_sum = sum(arr[:k])
    if any(primes[x] for x in arr[:k]):
        max_avg = window_sum / k
        max_idx = 0

    # Slide the window
    for i in range(k, n):
        window_sum = window_sum - arr[i-k] + arr[i]
        if any(primes[x] for x in arr[i-k+1:i+1]):
            avg = window_sum / k
            if avg > max_avg:
                max_avg = avg
                max_idx = i - k + 1
    
    return max_avg, max_idx