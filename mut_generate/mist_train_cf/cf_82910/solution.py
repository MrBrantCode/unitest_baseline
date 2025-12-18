"""
QUESTION:
Given a binary array `A` and an integer `K`, write a function `longestOnes` that returns the maximum length of a continuous subarray with all 1s after at most `K` zeros can be flipped to 1s. 

The function should take two parameters: `A` (the binary array) and `K` (the maximum number of zeros that can be flipped). The function should return an integer representing the maximum length of a continuous subarray with all 1s.

Constraints: 
1 <= A.length <= 20000
0 <= K <= A.length
A[i] can only be 0 or 1
"""

def longestOnes(A, K):
    left, right = 0, 0
    for right in range(len(A)):
        K -= A[right] == 0
        if K < 0:
            K += A[left] == 0
            left += 1
    
    return right - left + 1