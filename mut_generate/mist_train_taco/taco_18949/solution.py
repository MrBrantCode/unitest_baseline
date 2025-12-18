"""
QUESTION:
B: Pivots

problem

Given a permutation of length N, a_1, a_2, ..., a_N, which is a permutation of integers from 1 to N. Also, Q queries are given in order for this permutation. In the i-th query, you have to do the following:

* The value q_i (1 \ leq q_i \ leq N) is given. In the permutation \\ {a_1, a_2, ..., a_N \\}, where L is the permutation on the left side of q_i and R is the permutation on the right side of q_i, the original permutation L \\ q_i \\ R is R \\ Change to q_i \\ L. That is, when q_ {i} = a_j, the permutations \\ {a_1, ..., a_ {j-1}, a_j, a_ {j + 1}, ..., a_N \\} are \\ { Change to a_ {j + 1}, ..., a_N, a_j, a_1, ..., a_ {j-1} \\}.



The permutations L and R may be empty. For example, if L is empty, change q_i \\ R to R \\ q_i. The same is true when R is empty.

Output the permutation after processing these Q queries in order for the given permutation on one line.

Input format


N Q
a_1 a_2 ... a_N
q_1 q_2 ... q_Q


All inputs are integers.

The first row gives the number of elements in the permutation N and the number of queries Q, separated by blanks. In the second line, permutations a_1, a_2, ..., a_N, in which integers from 1 to N are rearranged, are given separated by blanks. The third line gives Q queries, separated by blanks. q_i represents the i-th query.

Constraint

* 1 \ leq N \ leq 10 ^ 5
* 1 \ leq Q \ leq 10 ^ 5
* 1 \ leq a_i \ leq N
* a_i is different
* 1 \ leq q_i \ leq N



Output format

Output the permutation after processing all the queries in order on one line.

Input example 1


5 2
1 5 3 2 4
5 2


Output example 1


4 5 1 2 3

* The first query changes the permutation to \\ {3, 2, 4, 5, 1 \\}.
* The second query changes the permutation to \\ {4, 5, 1, 2, 3 \\}.



Input example 2


5 1
1 2 3 4 5
Five


Output example 2


5 1 2 3 4





Example

Input

5 2
1 5 3 2 4
5 2


Output

4 5 1 2 3
"""

def process_permutation(N, Q, A, queries):
    if N == 1:
        return A
    
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    
    for i in range(N - 1):
        R[A[i]] = A[i + 1]
        L[A[i + 1]] = A[i]
    
    lm = A[0]
    rm = A[-1]
    
    for q in queries:
        if q == rm:
            l = L[q]
            R[l] = 0
            L[q] = 0
            R[q] = lm
            L[lm] = q
            lm = q
            rm = l
        elif q == lm:
            r = R[q]
            L[r] = 0
            R[q] = 0
            L[q] = rm
            R[rm] = q
            lm = r
            rm = q
        else:
            (l, r) = (L[q], R[q])
            L[q] = rm
            R[q] = lm
            R[l] = 0
            L[r] = 0
            L[lm] = q
            R[rm] = q
            rm = l
            lm = r
    
    ans = []
    while lm != 0:
        ans.append(lm)
        lm = R[lm]
    
    return ans