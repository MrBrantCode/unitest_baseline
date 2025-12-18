"""
QUESTION:
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number. Implement a function `prefixesDivBy5` that returns a list of booleans where answer[i] is true if and only if N_i is divisible by both 5 and 7. The function should take into account the constraints that 1 <= A.length <= 30000 and A[i] is either 0 or 1.
"""

def prefixesDivBy5(A):
    res = []
    remainder = 0
    for i in A:
        remainder = (remainder << 1 | i) % 35  
        res.append(remainder == 0)
    return res