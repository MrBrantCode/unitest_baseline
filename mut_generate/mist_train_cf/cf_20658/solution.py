"""
QUESTION:
Write a function called `findEvenSum` that takes an array `arr`, an index `index`, a boolean `isOddIndex`, and a sum as parameters. The function should return the sum of all even elements in the array, considering only elements at even indices or even elements at odd indices that are greater than or equal to zero. The function should use a recursive approach to solve the problem.
"""

def findEvenSum(arr, index, isOddIndex, sum):
    if index == len(arr):
        return sum

    if arr[index] % 2 == 0 and (not isOddIndex or (isOddIndex and arr[index] >= 0)):
        sum += arr[index]

    return findEvenSum(arr, index + 1, not isOddIndex, sum)