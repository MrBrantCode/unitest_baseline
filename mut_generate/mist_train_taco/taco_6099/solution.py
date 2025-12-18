"""
QUESTION:
Permutation p is an ordered set of integers p_1,  p_2,  ...,  p_{n}, consisting of n distinct positive integers, each of them doesn't exceed n. We'll denote the i-th element of permutation p as p_{i}. We'll call number n the size or the length of permutation p_1,  p_2,  ...,  p_{n}.

The decreasing coefficient of permutation p_1, p_2, ..., p_{n} is the number of such i (1 ≤ i < n), that p_{i} > p_{i} + 1.

You have numbers n and k. Your task is to print the permutation of length n with decreasing coefficient k.


-----Input-----

The single line contains two space-separated integers: n, k (1 ≤ n ≤ 10^5, 0 ≤ k < n) — the permutation length and the decreasing coefficient.


-----Output-----

In a single line print n space-separated integers: p_1, p_2, ..., p_{n} — the permutation of length n with decreasing coefficient k. 

If there are several permutations that meet this condition, print any of them. It is guaranteed that the permutation with the sought parameters exists.


-----Examples-----
Input
5 2

Output
1 5 2 4 3

Input
3 0

Output
1 2 3

Input
3 2

Output
3 2 1
"""

def generate_permutation_with_decreasing_coefficient(n, k):
    permutation = []
    
    # Generate the first part of the permutation with decreasing elements
    for i in range(k):
        permutation.append(n - i)
    
    # Generate the second part of the permutation with increasing elements
    for i in range(k, n):
        permutation.append(i - k + 1)
    
    return permutation