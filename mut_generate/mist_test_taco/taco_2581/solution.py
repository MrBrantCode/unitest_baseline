"""
QUESTION:
There is a one-dimensional cellular automaton consisting of N cells. Cells are numbered from 0 to N − 1.

Each cell has a state represented as a non-negative integer less than M. The states of cells evolve through discrete time steps. We denote the state of the i-th cell at time t as S(i, t). The state at time t + 1 is defined by the equation

S(i, t + 1) = (A × S(i − 1, t) + B × S(i, t) + C × S(i + 1, t)) mod M,         (1)

where A, B and C are non-negative integer constants. For i < 0 or N ≤ i, we define S(i, t) = 0.

Given an automaton definition and initial states of cells, your mission is to write a program that computes the states of the cells at a specified time T.



Input

The input is a sequence of datasets. Each dataset is formatted as follows.

N M A B C T
S(0, 0) S(1, 0) ... S(N − 1, 0)


The first line of a dataset consists of six integers, namely N, M, A, B, C and T. N is the number of cells. M is the modulus in the equation (1). A, B and C are coefficients in the equation (1). Finally, T is the time for which you should compute the states.

You may assume that 0 < N ≤ 50, 0 < M ≤ 1000, 0 ≤ A, B, C < M and 0 ≤ T ≤ 109.

The second line consists of N integers, each of which is non-negative and less than M. They represent the states of the cells at time zero.

A line containing six zeros indicates the end of the input.

Output

For each dataset, output a line that contains the states of the cells at time T. The format of the output is as follows.

S(0, T) S(1, T) ... S(N − 1, T)

Each state must be represented as an integer and the integers must be separated by a space.

Example

Input

5 4 1 3 2 0
0 1 2 0 1
5 7 1 3 2 1
0 1 2 0 1
5 13 1 3 2 11
0 1 2 0 1
5 5 2 0 1 100
0 1 2 0 1
6 6 0 2 3 1000
0 1 2 0 1 4
20 1000 0 2 3 1000000000
0 1 2 0 1 0 1 2 0 1 0 1 2 0 1 0 1 2 0 1
30 2 1 0 1 1000000000
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
30 2 1 1 1 1000000000
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
30 5 2 3 1 1000000000
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0


Output

0 1 2 0 1
2 0 0 4 3
2 12 10 9 11
3 0 4 2 1
0 4 2 0 4 4
0 376 752 0 376 0 376 752 0 376 0 376 752 0 376 0 376 752 0 376
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 3 2 2 2 3 3 1 4 3 1 2 3 0 4 3 3 0 4 2 2 2 2 1 1 2 1 3 0
"""

from operator import mul

def dot(v1, v2):
    return sum(map(mul, v1, v2))

def mat_mul(A, B, m):
    tB = tuple(zip(*B))
    return [[dot(A_i, B_j) % m for B_j in tB] for A_i in A]

def mat_pow(X, n, m):
    s = len(X)
    A = [[0] * s for i in range(s)]
    for i in range(s):
        A[i][i] = 1
    while n > 0:
        if n & 1:
            A = mat_mul(A, X, m)
        X = mat_mul(X, X, m)
        n >>= 1
    return A

def compute_cellular_automaton_states(N, M, A, B, C, T, initial_states):
    X = [[0] * N for i in range(N)]
    X[0][0] = B
    X[0][1] = A
    for (i, X_i) in enumerate(X[1:N - 1], start=1):
        X_i[i - 1] = C
        X_i[i] = B
        X_i[i + 1] = A
    X[-1][-2] = C
    X[-1][-1] = B
    
    s = [initial_states]
    ans = mat_mul(s, mat_pow(X, T, M), M)
    return ans[0]