"""
QUESTION:
The new ITone 6 has been released recently and George got really keen to buy it. Unfortunately, he didn't have enough money, so George was going to work as a programmer. Now he faced the following problem at the work.

Given a sequence of n integers p_1, p_2, ..., p_{n}. You are to choose k pairs of integers:

 [l_1, r_1], [l_2, r_2], ..., [l_{k}, r_{k}] (1 ≤ l_1 ≤ r_1 < l_2 ≤ r_2 < ... < l_{k} ≤ r_{k} ≤ n; r_{i} - l_{i} + 1 = m), 

in such a way that the value of sum $\sum_{i = 1}^{k} \sum_{j = l_{i}}^{r_{i}} p_{j}$ is maximal possible. Help George to cope with the task.


-----Input-----

The first line contains three integers n, m and k (1 ≤ (m × k) ≤ n ≤ 5000). The second line contains n integers p_1, p_2, ..., p_{n} (0 ≤ p_{i} ≤ 10^9).


-----Output-----

Print an integer in a single line — the maximum possible value of sum.


-----Examples-----
Input
5 2 1
1 2 3 4 5

Output
9

Input
7 1 3
2 10 7 18 5 33 0

Output
61
"""

def max_sum_of_pairs(n, m, k, sequence):
    if m == 1:
        sequence.sort(reverse=True)
        return sum(sequence[:k])
    
    p = []
    summ = 0
    for i in range(m):
        summ += sequence[i]
    p.append(summ)
    
    for i in range(m, n):
        summ += sequence[i] - sequence[i - m]
        p.append(summ)
    
    r = p.copy()
    c = len(p)
    q = [0] * c
    
    for j in range(k):
        for i in range(j, c):
            q[i] = p[i]
            if i - m >= 0 and j > 0:
                q[i] += r[i - m]
            if i - 1 >= 0:
                q[i] = max(q[i - 1], q[i])
        r = q.copy()
    
    return r[-1]