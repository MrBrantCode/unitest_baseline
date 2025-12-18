"""
QUESTION:
Design a function `find_longest_increasing_subsequence(arr)` that takes an array of integers as input and returns the longest increasing subsequence. The function should not use any built-in sorting or searching functions and have a time complexity of O(n^2), where n is the length of the input array.
"""

def find_longest_increasing_subsequence(arr):
    n = len(arr)
    lengths = [1] * n
    previous = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                previous[i] = j

    max_length = 0
    max_index = -1
    for i in range(n):
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i

    subsequence = []
    while max_index != -1:
        subsequence.append(arr[max_index])
        max_index = previous[max_index]
    subsequence.reverse()

    return subsequence