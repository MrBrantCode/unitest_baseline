"""
QUESTION:
Write a function `lenLongestFibSubseq(arr)` that determines the length of the longest subsequence of a given strictly ascending array `arr` that exhibits Fibonacci-like properties. The array `arr` is composed of positive integers and has a length of at least 3 and at most 1000. Each element in the array is a positive integer less than or equal to 10^9. The function should return the length of the longest Fibonacci-like subsequence if it exists, otherwise return 0.
"""

def lenLongestFibSubseq(arr):
    index = {x: i for i, x in enumerate(arr)}
    dp = [[2] * len(arr) for _ in arr]
    for j, x in enumerate(arr):
        for i in range(j):
            if x - arr[i] < arr[i] and x - arr[i] in index:
                dp[i][j] = dp[index[x - arr[i]]][i] + 1
    return max(x for row in dp for x in row) if max(x for row in dp for x in row) > 2 else 0