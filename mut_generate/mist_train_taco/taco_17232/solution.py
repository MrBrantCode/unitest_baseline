"""
QUESTION:
You are given a sequence of N integer numbers A. Calculate the sum of A_{i} AND A_{j} for all the pairs (i, j) where i < j. 
The AND operation is the Bitwise AND operation, defined as in here. 

------ Input ------ 

The first line of input consists of the integer N. 

The second line contains N integer numbers - the sequence A.

------ Output ------ 

Output the answer to the problem on the first line of the output.

------ Scoring ------ 

Subtask 1 (13 points): N ≤ 1000, A_{i} ≤ 1. 

Subtask 2 (39 points): N ≤ 1000, A_{i} ≤ 10^{9}. 

Subtask 3 (21 points): N ≤ 10^{5}, A_{i} ≤ 1. 

Subtask 4 (27 points): N ≤ 10^{5}, A_{i} ≤ 10^{6}. 

----- Sample Input 1 ------ 
5
1 2 3 4 5
----- Sample Output 1 ------ 
9
"""

def calculate_bitwise_and_sum(A, N=None):
    if N is None:
        N = len(A)
    
    res = 0
    count = 0
    
    for i in range(32):
        for j in range(N):
            if A[j] & 1:
                count += 1
            A[j] >>= 1
        res += count * (count - 1) // 2 * 2 ** i
        count = 0
    
    return res