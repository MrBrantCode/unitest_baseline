"""
QUESTION:
Write a function `sum_of_squares(arr)` that calculates the sum of the squares of the numbers in the given array using only loops. The function should have a time complexity of O(n^2), where n is the length of the array. The array can have duplicates, negative numbers, and can be empty.
"""

def entrance(arr):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                total += arr[i] * arr[j]
    return total