"""
QUESTION:
You are given a permutation p of length n. Remove one element from permutation to make the number of records the maximum possible.

We remind that in a sequence of numbers a_1, a_2, ..., a_{k} the element a_{i} is a record if for every integer j (1 ≤ j < i) the following holds: a_{j} < a_{i}. 


-----Input-----

The first line contains the only integer n (1 ≤ n ≤ 10^5) — the length of the permutation.

The second line contains n integers p_1, p_2, ..., p_{n} (1 ≤ p_{i} ≤ n) — the permutation. All the integers are distinct.


-----Output-----

Print the only integer — the element that should be removed to make the number of records the maximum possible. If there are multiple such elements, print the smallest one.


-----Examples-----
Input
1
1

Output
1

Input
5
5 1 2 3 4

Output
5



-----Note-----

In the first example the only element can be removed.
"""

def find_optimal_removal(n, p):
    if n == 1:
        return p[0]
    elif n == 2:
        return min(p[0], p[1])
    
    d = {}
    for i in p:
        d[i] = 0
    
    t = [max(p[0], p[1]), min(p[0], p[1])]
    if p[1] > p[0]:
        d[p[1]] -= 1
        d[p[0]] -= 1
    
    for i in p[2:]:
        if i > t[0]:
            t = [i, t[0]]
            d[i] -= 1
        elif i > t[1]:
            d[t[0]] += 1
            t = [t[0], i]
    
    (a, b) = (-2, n + 1)
    for i in d:
        if d[i] > a:
            a = d[i]
            b = i
        elif d[i] == a:
            if i < b:
                b = i
    
    return b