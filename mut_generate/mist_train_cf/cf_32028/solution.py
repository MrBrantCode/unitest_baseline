"""
QUESTION:
Write a function `nearest_smaller_to_right(arr)` that takes an array of integers `arr` as input and returns an array `vector` where each element at index `i` represents the nearest smaller element to the right of `arr[i]`. If there is no smaller element to the right of `arr[i]`, the value at index `i` in `vector` should be -1.
"""

def nearest_smaller(arr):
    stack = []
    vector = []
    for i in range(len(arr)-1, -1, -1):
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            vector.append(-1)
        else:
            vector.append(stack[-1])
        stack.append(arr[i])
    vector.reverse()
    return vector