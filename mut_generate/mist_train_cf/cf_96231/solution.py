"""
QUESTION:
Write a function `findEvenSum` that calculates the sum of all even elements in an array, considering only even elements at odd indices if they are non-negative. The function should use a recursive approach and handle cases where the array contains negative numbers. The function should take the following parameters: `arr`, the input array; `index`, the current index being considered; `isOddIndex`, a boolean flag indicating whether the current index is odd or even; and `sum`, the current sum of even elements found so far.
"""

def findEvenSum(arr, index=0, isOddIndex=True, sum=0):
    if index == len(arr):
        return sum

    if arr[index] % 2 == 0 and (not isOddIndex or (isOddIndex and arr[index] >= 0)):
        sum += arr[index]

    return findEvenSum(arr, index + 1, not isOddIndex, sum)