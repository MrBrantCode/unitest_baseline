"""
QUESTION:
Create a function named `segment_sequence` that takes a list of real numbers `S` as input and segments it into two non-empty lists such that the difference between the sum of the first list and the sum of the second list is a prime number. The function must maintain the original order of elements in `S` and return the two segments if a valid partition is found, or a message indicating that no valid segment was found.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def segment_sequence(S):
    cumulative_sum = [0]
    for num in S:
        cumulative_sum.append(cumulative_sum[-1] + num)
    for i in range(1, len(S)):
        if is_prime(cumulative_sum[i]) and is_prime(cumulative_sum[-1] - cumulative_sum[i]):
            return S[:i], S[i:]
    return "No valid segment found!"