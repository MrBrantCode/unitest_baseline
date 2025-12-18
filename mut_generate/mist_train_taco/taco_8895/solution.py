"""
QUESTION:
You are given N integers A_1, A_2, ..., A_N.

Consider the sums of all non-empty subsequences of A. There are 2^N - 1 such sums, an odd number.

Let the list of these sums in non-decreasing order be S_1, S_2, ..., S_{2^N - 1}.

Find the median of this list, S_{2^{N-1}}.

Constraints

* 1 \leq N \leq 2000
* 1 \leq A_i \leq 2000
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the median of the sorted list of the sums of all non-empty subsequences of A.

Examples

Input

3
1 2 1


Output

2


Input

1
58


Output

58
"""

def find_median_of_subsequence_sums(N, A):
    d = (sum(A) + 1) // 2
    c = 1
    for x in A:
        c |= c << x
    c >>= d
    for i in range(d + 5):
        if c & 1 << i:
            return d + i