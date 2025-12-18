"""
QUESTION:
Create a function `array_to_sequence` that takes an array of integers as input and returns an array representing a sequence where the sum of each consecutive pair of elements is a prime number. If no such sequence exists, return an empty array. The input array may contain duplicate elements and the sequence should be one of the permutations of the input array.
"""

from itertools import permutations

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def array_to_sequence(arr):
    for seq in permutations(arr):
        prime_sum = True
        for i in range(len(seq)-1):
            if not is_prime(seq[i] + seq[i+1]):
                prime_sum = False
                break
        if prime_sum:
            return list(seq)
    return []