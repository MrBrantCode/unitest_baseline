"""
QUESTION:
Write a function `longest_subarray` that takes two inputs: an array of integers and an integer K. The function should find the length of the longest subarray in the input array that has an equal number of 0's and 1's, an equal number of even and odd numbers, and a maximum length of K.
"""

def longest_subarray(arr, K):
    max_len = 0
    count = 0
    prefix_sum = [0]
    prefix_count = {}
    prefix_count[0] = -1

    for i, num in enumerate(arr):
        if num % 2 == 0:
            count += 1
        else:
            count -= 1

        prefix_sum.append(count)

        if count not in prefix_count:
            prefix_count[count] = i

        if count in prefix_count and i - prefix_count[count] <= K:
            max_len = max(max_len, i - prefix_count[count])

    return max_len