"""
QUESTION:
Write a function `find_sum_of_four(array, n)` that takes an array of integers and an integer `n` as parameters. The function should return the indices of the four numbers in the array whose sum equals `n`, or `None` if no such combination exists. The function must have a time complexity of O(n^3) and cannot use any additional data structures or sorting algorithms.
"""

def find_sum_of_four(array, n):
    length = len(array)
    for i in range(length - 3):
        for j in range(i + 1, length - 2):
            for k in range(j + 1, length - 1):
                for l in range(k + 1, length):
                    if array[i] + array[j] + array[k] + array[l] == n:
                        return [i, j, k, l]
    return None