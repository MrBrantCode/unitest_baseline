"""
QUESTION:
Write a function `sumOddLengthSubarrays` that calculates the sum of all possible odd-length subarrays in a given array `arr` of positive integers and finds the maximum sum among these odd-length subarrays. The function should return a tuple containing the sum of all odd-length subarrays and the maximum sum. The input array `arr` will have a length between 1 and 100, and each element in the array will be between 1 and 1000.
"""

def sumOddLengthSubarrays(arr):
    total_sum = 0
    max_sum = 0
    l = len(arr)
    for i in range(l):
        for j in range(i + 1, l + 1, 2):                
            total_sum += sum(arr[i:j])
            max_sum = max(max_sum, sum(arr[i:j]))
    return (total_sum, max_sum)