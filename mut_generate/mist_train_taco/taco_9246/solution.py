"""
QUESTION:
Shil has a permutation p1 , p2 .. pN of numbers from 1 to N and M queries. Each query consists of two integers l and  r . Answer to each query is total number of pairs[i , j] such that l ≤ i ≤ j ≤ r and|pi - pj| ≤ D. 

INPUT:
First line consists of three integers N, M and D. Next line consists of permutation p1 , p2 .. pN of the first N natural numbers. Next M lines consists of two integers l and r . 

OUTPUT:
Output M integers with i^th integer corresponding answer to i^th query.

CONSTRAINTS:
1 ≤ N, M ≤ 10^5
1 ≤ D ≤ 10
1 ≤ pi ≤ N 
1 ≤ l ≤ r ≤ N

SAMPLE INPUT
5 5 1
1 4 2 3 5
1 3
2 4
1 5
2 2
4 5

SAMPLE OUTPUT
4
5
9
1
2

Explanation

For 1^st query , all the pairs are (1,1) , (4,4) , (2,2) , (1,2).
For 2^nd query , all the pairs are (4,4) , (2,2) , (3,3) , (4,3) , (2,3).
For 3^rd query , all the pairs are (1,1) , (4,4) , (2,2) , (3,3) , (5,5) , (1,2) , (4,5) , (4,3) , (2,3).
Note that numbers in the bracket are values not indices of permutation.
"""

def count_valid_pairs(n, m, d, permutation, queries):
    pos = [0] * (n + 1)
    for i in range(n):
        pos[permutation[i]] = i

    q = sorted([((l, r), i) for i, (l, r) in enumerate(queries)], key=lambda tp: tp[0][1])

    tree = [0] * (n + 1)

    def update(pos):
        while pos <= n:
            tree[pos] += 1
            pos += pos & (-pos)

    def query(pos):
        ans = 0
        while pos > 0:
            ans += tree[pos]
            pos -= pos & (-pos)
        return ans

    j = 0
    ans = [0] * m
    for i in range(1, n + 1):
        for v in range(max(1, permutation[i - 1] - d), min(n + 1, permutation[i - 1] + d + 1)):
            if pos[v] + 1 <= i:
                update(pos[v] + 1)
        while j < len(q) and q[j][0][1] == i:
            ans[q[j][1]] = query(q[j][0][1]) - query(q[j][0][0] - 1)
            j += 1

    return ans