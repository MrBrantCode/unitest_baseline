"""
QUESTION:
Write a function `find_sum_of_four(array, n)` that checks if the sum of any four elements in the given array equals the parameter `n`. The function should return the indices of the four numbers whose sum equals `n`. The time complexity of the function should be O(n^3) and it should not use any additional data structures or sorting algorithms.
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