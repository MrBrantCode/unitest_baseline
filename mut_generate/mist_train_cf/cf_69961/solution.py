"""
QUESTION:
Given an array of positive integers `arr`, find the minimum sum of non-leaf node values for all possible binary trees where each non-leaf node's value is the product of the highest leaf value in its left and right subtrees, and the elements of `arr` match the values of each leaf in an in-order traversal of the tree.

Implement the `mctFromLeafValues` function with the following restrictions: `2 <= arr.length <= 40` and `1 <= arr[i] <= 15`. The answer should fit within a 32-bit signed integer.
"""

def mctFromLeafValues(arr):
    res = 0
    stack = [float('inf')]
    for a in arr:
        while stack[-1] <= a:
            mid = stack.pop()
            res += mid * min(stack[-1], a)
        stack.append(a)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res