"""
QUESTION:
Construct a function called `uncommon_elements` that takes a list of positive integers as input. The function should return a list of unique integers that meet two conditions: 
- The integer's frequency in the list is more than half of its value.
- The count of the integer's occurrence in the list is a prime number.
If no such integers are found, the function should return an empty list.
"""

from collections import Counter

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def uncommon_elements(sequence):
    sequence_count = Counter(sequence)
    res = []
    for elem, count in sequence_count.items():
        if count > elem / 2 and is_prime(count):
            res.append(elem)
    return res