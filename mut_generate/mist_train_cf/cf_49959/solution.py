"""
QUESTION:
Write a function `sortArrayByParity` that takes an array `A` of non-negative integers as input and returns an array consisting of all the even elements of `A`, followed by all the odd elements of `A`. The even elements should be sorted in ascending order and the odd elements in descending order. The function must work with arrays of length between 1 and 5000 (inclusive) and with integers between 0 and 5000 (inclusive).
"""

def sortArrayByParity(A):
    return sorted(A, key=lambda x: (x % 2, -x if x % 2 else x))