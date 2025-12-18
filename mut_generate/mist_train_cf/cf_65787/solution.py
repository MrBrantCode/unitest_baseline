"""
QUESTION:
Implement a function `min_set(arr, K)` that finds the minimum set of numbers from a given set of numbers `arr` such that the sum of the selected numbers is equal to a given value `K`, using a greedy algorithm. The function should return a list of the selected numbers. The input set `arr` contains distinct positive integers and `K` is a non-negative integer.
"""

def min_set(arr, K):
    arr.sort(reverse=True)  # sort the array in descending order
    result = []

    for i in arr:
        while (K >= i):  # while the element can be subtracted from K
            K -= i  # subtract it from K
            result.append(i)  # and add it to the result

    return result  # return the result set