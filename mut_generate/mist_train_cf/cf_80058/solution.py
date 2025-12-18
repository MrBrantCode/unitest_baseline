"""
QUESTION:
Write a function `sortArrayByParity` that takes an array `A` of non-negative integers as input and returns a new array where all the even elements of `A` are placed before all the odd elements of `A`. The order of elements within the even and odd groups can be arbitrary. The input array `A` has a length within the range of `1 <= A.length <= 5000` and its elements are within the range of `0 <= A[i] <= 5000`.
"""

def sortArrayByParity(A):
    evens = []
    odds = []
    for num in A:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds