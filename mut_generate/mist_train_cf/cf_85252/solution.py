"""
QUESTION:
Implement a function named `lcm_list` that takes two integer arrays of unspecified lengths as input and returns their Least Common Multiple (LCM) using the Extended Euclidean algorithm. The LCM should be calculated for the GCDs of the input arrays, not for all possible combinations of numbers from both arrays. The function should be able to handle any valid input arrays of integers.
"""

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def extendedEuclidean(arr):
    num1 = arr[0]
    for i in range(1,len(arr)):
        num1 = gcd(num1,arr[i])
    return num1

def lcm(x, y):
    return abs(x*y) // gcd(x, y)

def lcm_list(arr1, arr2):
    gcd1 = extendedEuclidean(arr1)
    gcd2 = extendedEuclidean(arr2)
    return lcm(gcd1, gcd2)