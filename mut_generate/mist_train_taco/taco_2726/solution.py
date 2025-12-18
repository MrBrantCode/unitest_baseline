"""
QUESTION:
There are N squares lining up in a row, numbered 1 through N from left to right. Initially, all squares are white. We also have N-1 painting machines, numbered 1 through N-1. When operated, Machine i paints Square i and i+1 black.

Snuke will operate these machines one by one. The order in which he operates them is represented by a permutation of (1, 2, ..., N-1), P, which means that the i-th operated machine is Machine P_i.

Here, the score of a permutation P is defined as the number of machines that are operated before all the squares are painted black for the first time, when the machines are operated in the order specified by P. Snuke has not decided what permutation P to use, but he is interested in the scores of possible permutations. Find the sum of the scores over all possible permutations for him. Since this can be extremely large, compute the sum modulo 10^9+7.

Constraints

* 2 \leq N \leq 10^6

Input

Input is given from Standard Input in the following format:


N


Output

Print the sum of the scores over all possible permutations, modulo 10^9+7.

Examples

Input

4


Output

16


Input

2


Output

1


Input

5


Output

84


Input

100000


Output

341429644
"""

def calculate_total_score(N):
    LARGE = 10**9 + 7
    
    def ex_euclid(x, y):
        (c0, c1) = (x, y)
        (a0, a1) = (1, 0)
        (b0, b1) = (0, 1)
        while c1 != 0:
            m = c0 % c1
            q = c0 // c1
            (c0, c1) = (c1, m)
            (a0, a1) = (a1, a0 - q * a1)
            (b0, b1) = (b1, b0 - q * b1)
        return (c0, a0, b0)
    
    N -= 1  # Adjust N to represent the number of machines
    
    fac_list = [1] * (N + 1)
    fac = 1
    for i in range(1, N + 1):
        fac = fac * i % LARGE
        fac_list[i] = fac
    
    fac_inv_list = [1] * (N + 1)
    for i in range(N + 1):
        fac_inv_list[i] = pow(fac_list[i], LARGE - 2, LARGE)
    
    def nCr(n, r):
        return fac_list[n] * fac_inv_list[r] % LARGE * fac_inv_list[n - r] % LARGE
    
    pat = 0
    score = 0
    for k in range(N + 1):
        if k - 1 >= N - k:
            res = fac_list[k - 1] * fac_list[k] % LARGE * fac_inv_list[k - 1 - N + k] % LARGE
            score = (score + (res - pat) * k) % LARGE
            pat = res
    
    return score