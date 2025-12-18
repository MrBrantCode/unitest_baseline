"""
QUESTION:
You are given a sequence (P_1,P_2,...,P_N) which is a permutation of the integers from 1 through N. You would like to sort this sequence in ascending order by repeating the following operation:

* Choose an element in the sequence and move it to the beginning or the end of the sequence.



Find the minimum number of operations required. It can be proved that it is actually possible to sort the sequence using this operation.

Constraints

* 1 \leq N \leq 2\times 10^5
* (P_1,P_2,...,P_N) is a permutation of (1,2,...,N).
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
P_1
:
P_N


Output

Print the minimum number of operations required.

Examples

Input

4
1
3
2
4


Output

2


Input

6
3
2
5
1
4
6


Output

4


Input

8
6
3
1
2
7
4
8
5


Output

5
"""

def minimum_operations_to_sort_permutation(P):
    N = len(P)
    L = [1] * (N + 1)
    
    for i in range(N):
        if P[i] < N and L[P[i] + 1] == 1:
            L[P[i] + 1] = L[P[i]] + 1
        if L[P[i]] == 1:
            L[P[i]] = 0
    
    ans = N - max(L)
    return ans