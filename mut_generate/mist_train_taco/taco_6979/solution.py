"""
QUESTION:
You are given an integer m as a product of integers a1, a2, ... an <image>. Your task is to find the number of distinct decompositions of number m into the product of n ordered positive integers.

Decomposition into n products, given in the input, must also be considered in the answer. As the answer can be very large, print it modulo 1000000007 (109 + 7).

Input

The first line contains positive integer n (1 ≤ n ≤ 500). The second line contains space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109).

Output

In a single line print a single number k — the number of distinct decompositions of number m into n ordered multipliers modulo 1000000007 (109 + 7).

Examples

Input

1
15


Output

1


Input

3
1 1 2


Output

3


Input

2
5 7


Output

4

Note

In the second sample, the get a decomposition of number 2, you need any one number out of three to equal 2, and the rest to equal 1.

In the third sample, the possible ways of decomposing into ordered multipliers are [7,5], [5,7], [1,35], [35,1].

A decomposition of positive integer m into n ordered multipliers is a cortege of positive integers b = {b1, b2, ... bn} such that <image>. Two decompositions b and c are considered different, if there exists index i such that bi ≠ ci.
"""

from collections import Counter

def count_distinct_decompositions(n, a):
    mod = 10 ** 9 + 7
    
    # Precompute factorials and their inverses modulo mod
    fac = [1]
    for ii in range(1, 10 ** 5 + 1):
        fac.append(fac[-1] * ii % mod)
    
    fac_in = [pow(fac[-1], mod - 2, mod)]
    for ii in range(10 ** 5, 0, -1):
        fac_in.append(fac_in[-1] * ii % mod)
    fac_in.reverse()
    
    # Function to factorize a number and update the counter
    def factor(x, cou):
        while not x % 2:
            x //= 2
            cou[2] += 1
        for i in range(3, int(x ** 0.5) + 1, 2):
            while not x % i:
                x //= i
                cou[i] += 1
        if x != 1:
            cou[x] += 1
    
    # Factorize each number in the list
    cou = Counter()
    for i in a:
        factor(i, cou)
    
    # Calculate the number of distinct decompositions
    ans = 1
    for i in cou:
        a_val = cou[i] + n - 1
        b_val = n - 1
        ans = ans * fac[a_val] * fac_in[b_val] * fac_in[a_val - b_val] % mod
    
    return ans