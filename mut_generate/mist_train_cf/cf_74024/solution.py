"""
QUESTION:
Implement the function `canMakeArithmeticProgression` to determine whether an array of integers can be rearranged to form an arithmetic progression. The function should take an array of integers as input and return `True` if the array can be rearranged to form an arithmetic progression and `False` otherwise. The input array will have a length between 2 and 1000, inclusive, and will contain integers ranging from -10^6 to 10^6, inclusive. The array may contain duplicate elements.
"""

def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True