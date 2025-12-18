"""
QUESTION:
Implement a function `max_subarray_sum` that takes an array of integers and an integer `k` as input. The function should return the maximum sum of a subarray with a length greater than or equal to `k`. The function should have a time complexity of O(n) and space complexity of O(1), where n is the size of the input array.
"""

def max_subarray_sum(arr, k):
    start = 0
    end = 0
    maxSum = 0
    currentSum = 0

    while end < len(arr):
        currentSum += arr[end]
        if currentSum > maxSum:
            maxSum = currentSum

        if end - start + 1 >= k:
            if currentSum > 0:
                currentSum -= arr[start]
                start += 1
            else:
                start = end + 1
                currentSum = 0

        end += 1

    return maxSum