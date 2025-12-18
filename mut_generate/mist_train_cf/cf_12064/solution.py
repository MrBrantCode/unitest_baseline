"""
QUESTION:
Write a function `count_quadruples` that takes a list of integers as input and returns the number of quadruples in the list that sum up to zero. The function should have a time complexity of O(n^4), where n is the length of the input list. The input list can contain both positive and negative numbers, and a quadruple is defined as a set of four numbers in the list.
"""

def count_quadruples(arr):
    count = 0
    n = len(arr)
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == 0:
                        count += 1
    return count