"""
QUESTION:
Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)
Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

 



Example 1:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.


Example 2:
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.


Example 3:
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

 
Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""

def max_sum_two_no_overlap(A, L, M):
    N = len(A)
    if L + M > N:
        return -1

    def findmax(L, M):
        sL = [sum(A[:L])]
        for i in range(L, N - M):
            tmp = sL[-1] + A[i] - A[i - L]
            sL.append(tmp)
        sLmax = [sL[0]]
        for i in range(1, len(sL)):
            if sL[i] > sLmax[-1]:
                sLmax.append(sL[i])
            else:
                sLmax.append(sLmax[-1])
        sM = [sum(A[-M:])]
        for i in range(N - M - 1, L - 1, -1):
            tmp = sM[-1] + A[i] - A[i + M]
            sM.append(tmp)
        sMmax = [sM[0]]
        for i in range(1, len(sM)):
            if sM[i] > sMmax[-1]:
                sMmax.append(sM[i])
            else:
                sMmax.append(sMmax[-1])
        sMax = [sum(x) for x in zip(sLmax, sMmax[::-1])]
        m = max(sMax)
        return m
    
    if L == M:
        return findmax(L, M)
    else:
        return max(findmax(L, M), findmax(M, L))