"""
QUESTION:
You are given a permutation p of the set {1, 2, ..., N}. Please construct two sequences of positive integers a_1, a_2, ..., a_N and b_1, b_2, ..., b_N satisfying the following conditions:

* 1 \leq a_i, b_i \leq 10^9 for all i
* a_1 < a_2 < ... < a_N
* b_1 > b_2 > ... > b_N
* a_{p_1}+b_{p_1} < a_{p_2}+b_{p_2} < ... < a_{p_N}+b_{p_N}

Constraints

* 2 \leq N \leq 20,000
* p is a permutation of the set {1, 2, ..., N}

Input

The input is given from Standard Input in the following format:


N
p_1 p_2 ... p_N


Output

The output consists of two lines. The first line contains a_1, a_2, ..., a_N seperated by a space. The second line contains b_1, b_2, ..., b_N seperated by a space.

It can be shown that there always exists a solution for any input satisfying the constraints.

Examples

Input

2
1 2


Output

1 4
5 4


Input

3
3 2 1


Output

1 2 3
5 3 1


Input

3
2 3 1


Output

5 10 100
100 10 1
"""

def construct_sequences(N, p):
    # Initialize sequences a and b
    a = [20001 * i for i in range(1, N + 1)]
    b = [20001 * (N + 1 - i) for i in range(1, N + 1)]
    
    # Adjust b based on the permutation p
    for i in range(N):
        b[p[i] - 1] += i
    
    return a, b