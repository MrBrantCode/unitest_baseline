"""
QUESTION:
You are given two arrays A and B each of length N. You can perform the following operation on array A zero or more times. 
	Select any two indices i and j, 1 <= i , j <= N and i != j
	Set A[i] = A[i] + 2 and A[j] = A[j]-2 
Find the minimum number of operations required to make A and B equal.
Note :
	Two arrays are said to be equal if the frequency of each element is equal in both of them.
	Arrays may contain duplicate elements.
Example 1:
Input:
N = 3
A[] = {2, 5, 6}
B[] = {1, 2, 10}
Output: 2
Explanation: 
Select i = 3, j = 2, A[3] = 6 + 2 = 8 and A[2] = 5 - 2 = 3
Select i = 3, j = 2, A[3] = 8 + 2 = 10 and A[2] = 3 - 2 = 1
Now A = {2, 1, 10} and B = {1, 2, 10}
Example 2:
Input:
N = 2
A[] = {3, 3}
B[] = {9, 8}
Output: -1
Explanation: 
It can be shown that A cannot be made equal to B.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes the 2 arrays A[], B[] and their size N as input parameters and returns the minimum number of moves to make A and B equal if possible else return -1.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
-10^{9} <= A[i] <= 10^{9}
-10^{9} <= B[i] <= 10^{9}
"""

from typing import List

def min_operations_to_equal_arrays(A: List[int], B: List[int]) -> int:
    N = len(A)
    if N != len(B):
        return -1
    
    if sum(A) != sum(B):
        return -1
    
    A.sort()
    B.sort()
    
    ae, ao, be, bo = [], [], [], []
    
    for i in range(N):
        if A[i] % 2:
            ao.append(A[i])
        else:
            ae.append(A[i])
        
        if B[i] % 2:
            bo.append(B[i])
        else:
            be.append(B[i])
    
    if len(ao) != len(bo) or len(ae) != len(be):
        return -1
    
    osum, esum = 0, 0
    
    for i in range(len(ao)):
        osum += abs(ao[i] - bo[i])
    
    for i in range(len(ae)):
        esum += abs(ae[i] - be[i])
    
    if osum % 2 or esum % 2:
        return -1
    else:
        return (osum + esum) // 4