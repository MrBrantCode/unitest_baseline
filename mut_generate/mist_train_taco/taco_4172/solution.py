"""
QUESTION:
Little Dima has two sequences of points with integer coordinates: sequence (a1, 1), (a2, 2), ..., (an, n) and sequence (b1, 1), (b2, 2), ..., (bn, n).

Now Dima wants to count the number of distinct sequences of points of length 2·n that can be assembled from these sequences, such that the x-coordinates of points in the assembled sequence will not decrease. Help him with that. Note that each element of the initial sequences should be used exactly once in the assembled sequence.

Dima considers two assembled sequences (p1, q1), (p2, q2), ..., (p2·n, q2·n) and (x1, y1), (x2, y2), ..., (x2·n, y2·n) distinct, if there is such i (1 ≤ i ≤ 2·n), that (pi, qi) ≠ (xi, yi).

As the answer can be rather large, print the remainder from dividing the answer by number m.

Input

The first line contains integer n (1 ≤ n ≤ 105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109). The third line contains n integers b1, b2, ..., bn (1 ≤ bi ≤ 109). The numbers in the lines are separated by spaces.

The last line contains integer m (2 ≤ m ≤ 109 + 7).

Output

In the single line print the remainder after dividing the answer to the problem by number m. 

Examples

Input

1
1
2
7


Output

1


Input

2
1 2
2 3
11


Output

2

Note

In the first sample you can get only one sequence: (1, 1), (2, 1). 

In the second sample you can get such sequences : (1, 1), (2, 2), (2, 1), (3, 2); (1, 1), (2, 1), (2, 2), (3, 2). Thus, the answer is 2.
"""

from collections import defaultdict

def factorial(n, m, rep):
    r = 1
    for i in range(2, n + 1):
        j = i
        while j % 2 == 0 and rep > 0:
            j = j // 2
            rep -= 1
        r *= j
        r %= m
    return r

def count_distinct_sequences(n, a, b, m):
    ans = 1
    d = defaultdict(lambda: 0)
    e = defaultdict(lambda: 0)
    
    for i in range(n):
        d[a[i]] += 1
        d[b[i]] += 1
        if a[i] == b[i]:
            e[a[i]] += 1
    
    for key in d:
        k = d[key]
        rep = e[key]
        ans = ans * factorial(k, m, rep)
        ans = ans % m
    
    return int(ans)