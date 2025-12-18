"""
QUESTION:
Write a function `sum_xor_pairs` and another function `sum_and_pairs` that calculate the sum of XOR operation and bitwise AND operation for all pairs of numbers in the given list respectively. The functions should take a list of integers as input and return the sum of the XOR operation and the sum of the bitwise AND operation for all pairs of numbers in the list.
"""

def sum_xor_pairs(lst):
    n = len(lst)
    sum_xor = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            sum_xor += lst[i] ^ lst[j]
    return sum_xor

def sum_and_pairs(lst):
    n = len(lst)
    sum_and = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            sum_and += lst[i] & lst[j]
    return sum_and