"""
QUESTION:
You are given N integers; the i-th of them is A_i. Find the maximum possible sum of the absolute differences between the adjacent elements after arranging these integers in a row in any order you like.

Constraints

* 2 \leq N \leq 10^5
* 1 \leq A_i \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1
:
A_N


Output

Print the maximum possible sum of the absolute differences between the adjacent elements after arranging the given integers in a row in any order you like.

Examples

Input

5
6
8
1
2
3


Output

21


Input

6
3
1
4
1
5
9


Output

25


Input

3
5
5
1


Output

8
"""

def max_adjacent_difference_sum(A):
    N = len(A)
    A.sort()
    
    if N % 2 == 0:
        return 2 * (sum(A[N // 2:]) - sum(A[:N // 2])) - (A[N // 2] - A[N // 2 - 1])
    else:
        return 2 * (sum(A[N // 2 + 1:]) - sum(A[:N // 2])) - min(A[N // 2] - A[N // 2 - 1], A[N // 2 + 1] - A[N // 2])