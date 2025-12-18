"""
QUESTION:
Write a function `maxWidthRamp` that takes an array `A` of integers as input and returns a tuple containing the maximum width of a ramp in `A` and the sum of all elements between the start and end indices of the maximum width ramp. A ramp is a tuple `(i, j)` for which `i < j` and `A[i] <= A[j]`. The width of such a ramp is `j - i`. If no such ramp exists, return `(0, 0)`. The length of `A` is between 2 and 50000 (inclusive), and each element in `A` is between 0 and 50000 (inclusive).
"""

def maxWidthRamp(A):
    stack = []
    for i, num in enumerate(A):
        if not stack or A[stack[-1]] > num:
            stack.append(i)
    maxWidth = 0
    maxSum = 0
    prefixSum = [0] * len(A)
    prefixSum[0] = A[0]
    for i in range(1, len(A)):
        prefixSum[i] = prefixSum[i-1] + A[i]
    for j in range(len(A)-1, -1, -1):
        while stack and A[stack[-1]] <= A[j]:
            i = stack.pop()
            if j - i > maxWidth:
                maxWidth = j - i
                if i > 0:
                    maxSum = prefixSum[j] - prefixSum[i-1]
                else:
                    maxSum = prefixSum[j]
    return maxWidth, maxSum