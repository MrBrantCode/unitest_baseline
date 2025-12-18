"""
QUESTION:
Given an array `arr` of integers, partition the array into chunks, sort each chunk individually, and concatenate the sorted chunks to form a new array. The goal is to determine the maximum number of chunks that can be created while ensuring that the concatenated result is a sorted array. The length of `arr` will be within the range `[1, 3000]` and each element `arr[i]` will be an integer within the range `[0, 10**9]`.
"""

def maxChunksToSorted(arr):
    stack = []
    for num in arr:
        if stack and num < stack[-1]:
            head = stack.pop()
            while stack and num < stack[-1]:
                stack.pop()
            stack.append(head)
        else:
            stack.append(num)
    return len(stack)