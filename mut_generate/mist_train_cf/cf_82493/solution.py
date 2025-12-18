"""
QUESTION:
Write a function `shortest_subseq(arr, threshold)` that takes a list of integers `arr` and an integer `threshold` as input. The function should return the shortest subsequence of odd elements from `arr` with a sum greater than `threshold`. If no such subsequence exists, return an empty list.
"""

def shortest_subseq(arr, threshold):
    min_len = float('inf')
    start = 0
    cur_sum = 0
    min_start = -1
    min_end = -1

    for end in range(len(arr)):
        if arr[end] % 2 == 1:  
            cur_sum += arr[end]

            while cur_sum > threshold:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start
                    min_end = end
                if arr[start] % 2 == 1:  
                    cur_sum -= arr[start]
                start += 1

    if min_start == -1:
        return []

    return arr[min_start:min_end+1]