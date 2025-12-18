"""
QUESTION:
Write a function `find_longest_subarray(arr)` that takes an array of integers or floating point numbers as input and returns the longest subarray with a sum of 0 or closest to zero. The function should have a time complexity of O(n), where n is the length of the array, and should handle arrays with repeated elements, negative numbers, zero, and up to 10^6 elements.
"""

def find_longest_subarray(arr):
    prefix_sum = {0: -1}
    max_length = 0
    sum = 0
    index = -1

    for i in range(len(arr)):
        sum += arr[i]

        if sum == 0:
            max_length = i + 1
            index = i

        if sum in prefix_sum:
            length = i - prefix_sum[sum]
            if length > max_length:
                max_length = length
                index = i

        if sum not in prefix_sum:
            prefix_sum[sum] = i

    return arr[index + 1 - max_length: index + 1]