"""
QUESTION:
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)
Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.
Example :
Input: 
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.

Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].
"""

def can_split_array_with_same_average(A):
    N = len(A)
    S = sum(A)
    
    if N == 1:
        return False
    
    A = [z * N - S for z in A]
    mid = N // 2
    left = {A[0]}
    right = {A[-1]}
    
    if not any((S * size % N == 0 for size in range(1, mid + 1))):
        return False
    
    for i in range(1, mid):
        left |= {z + A[i] for z in left} | {A[i]}
    
    for i in range(mid, N - 1):
        right |= {z + A[i] for z in right} | {A[i]}
    
    if 0 in left | right:
        return True
    
    left -= {sum(A[:mid])}
    return any((-ha in right for ha in left))