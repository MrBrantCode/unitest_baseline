"""
QUESTION:
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].



Note:

1 
0
"""

def find_max_length_of_common_subarray(A, B):
    def check(length):
        seen = {A[i:i + length] for i in range(len(A) - length + 1)}
        return any((B[j:j + length] in seen for j in range(len(B) - length + 1)))
    
    A = ''.join(map(chr, A))
    B = ''.join(map(chr, B))
    
    lo, hi = 0, min(len(A), len(B)) + 1
    
    while lo < hi:
        mi = (lo + hi) // 2
        if check(mi):
            lo = mi + 1
        else:
            hi = mi
    
    return lo - 1