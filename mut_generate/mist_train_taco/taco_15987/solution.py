"""
QUESTION:
Takahashi, who is a novice in competitive programming, wants to learn M algorithms.
Initially, his understanding level of each of the M algorithms is 0.
Takahashi is visiting a bookstore, where he finds N books on algorithms.
The i-th book (1\leq i\leq N) is sold for C_i yen (the currency of Japan). If he buys and reads it, his understanding level of the j-th algorithm will increase by A_{i,j} for each j (1\leq j\leq M).
There is no other way to increase the understanding levels of the algorithms.
Takahashi's objective is to make his understanding levels of all the M algorithms X or higher. Determine whether this objective is achievable. If it is achievable, find the minimum amount of money needed to achieve it.
"""

def minimum_cost_to_achieve_understanding(n, m, x, costs, understanding_levels):
    a = 10 ** 9
    
    for i in range(2 ** n):
        lm = [0] * m
        t = 0
        
        for j in range(n):
            if i >> j & 1:
                for k in range(m):
                    lm[k] += understanding_levels[j][k]
                t += costs[j]
        
        if all(s >= x for s in lm):
            a = min(a, t)
    
    return -1 if a == 10 ** 9 else a