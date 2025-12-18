"""
QUESTION:
Write a function `longest_valley(arr)` that takes an integer array `arr` as input and returns the length of the longest subarray that is a valley. A valley is defined as a subarray where there exists an index `i` such that `arr[0] > arr[1] > ... > arr[i-1] > arr[i] < arr[i+1] < ... < arr[arr.length-1]`. Return 0 if there is no valley subarray.

The array `arr` satisfies the following constraints: `1 <= arr.length <= 10^4` and `0 <= arr[i] <= 10^4`.
"""

def longest_valley(arr):
    n = len(arr)
    down, up, answer = 0, 0, 0
    for i in range(1, n):
        if arr[i]<arr[i-1]:
            if up:
                down = 0
            down += 1
            up = 0
        if arr[i]>arr[i-1] and down:
            up += 1
        if arr[i]==arr[i-1]:
            down = up = 0
        answer = max(answer, down + up + 1)
    return answer if answer>=3 else 0