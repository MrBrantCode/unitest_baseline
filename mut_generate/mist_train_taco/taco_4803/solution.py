"""
QUESTION:
Given are positive integers N and K.

Determine if the 3N integers K, K+1, ..., K+3N-1 can be partitioned into N triples (a_1,b_1,c_1), ..., (a_N,b_N,c_N) so that the condition below is satisfied. Any of the integers K, K+1, ..., K+3N-1 must appear in exactly one of those triples.

* For every integer i from 1 to N, a_i + b_i \leq c_i holds.



If the answer is yes, construct one such partition.

Constraints

* 1 \leq N \leq 10^5
* 1 \leq K \leq 10^9

Input

Input is given from Standard Input in the following format:


N K


Output

If it is impossible to partition the integers satisfying the condition, print `-1`. If it is possible, print N triples in the following format:


a_1 b_1 c_1
:
a_N b_N c_N

Output

If it is impossible to partition the integers satisfying the condition, print `-1`. If it is possible, print N triples in the following format:


a_1 b_1 c_1
:
a_N b_N c_N

Examples

Input

1 1


Output

1 2 3


Input

3 3


Output

-1
"""

def partition_triples(N, K):
    if 2 * K - 1 > N:
        return -1
    
    a = [i for i in range(K, K + N)]
    A = []
    for i in range(len(a)):
        if i % 2 == 0:
            A.append(a[i])
    for i in range(len(a)):
        if i % 2 == 1:
            A.append(a[i])
    
    b1 = [i for i in range(K + N, K + N + (N + 1) // 2)]
    b2 = [i for i in range(K + N + (N + 1) // 2, K + 2 * N)]
    b1.reverse()
    b2.reverse()
    B = b1 + b2
    
    C = [i for i in range(K + 2 * N, K + 3 * N)]
    
    result = [(A[i], B[i], C[i]) for i in range(N)]
    return result