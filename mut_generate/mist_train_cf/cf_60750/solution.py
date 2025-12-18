"""
QUESTION:
Write a function `first_irregular` that takes an array of integers as input and returns the first non-repeating integer which has an irregular frequency. A frequency is considered irregular if it is a prime number. If no such integer exists, return `None`. The function should iterate through the input array in order and return the first integer that meets the condition.
"""

from collections import Counter

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def first_irregular(arr):
    cnt = Counter(arr)
    for num in arr:
        if is_prime(cnt[num]):
            return num
    return None