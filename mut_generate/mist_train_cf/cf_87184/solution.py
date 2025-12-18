"""
QUESTION:
Create a function `longest_increasing_subsequence` that takes an array of integers as input and returns the longest increasing subsequence. The function should have a time complexity of O(n^2) and a space complexity of O(n). The input array contains at least one element. All elements in the array are integers. The function should not use any built-in functions or libraries to solve the problem.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    max_index = lis.index(max_length)

    subsequence = [arr[max_index]]
    length = max_length

    for i in range(max_index - 1, -1, -1):
        if lis[i] == length - 1 and arr[i] < subsequence[-1]:
            subsequence.append(arr[i])
            length -= 1

    return subsequence[::-1]