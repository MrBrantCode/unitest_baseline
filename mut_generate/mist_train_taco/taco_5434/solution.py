"""
QUESTION:
The Little Elephant loves playing with arrays. He has array a, consisting of n positive integers, indexed from 1 to n. Let's denote the number with index i as ai. 

Additionally the Little Elephant has m queries to the array, each query is characterised by a pair of integers lj and rj (1 ≤ lj ≤ rj ≤ n). For each query lj, rj the Little Elephant has to count, how many numbers x exist, such that number x occurs exactly x times among numbers alj, alj + 1, ..., arj.

Help the Little Elephant to count the answers to all queries.

Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 105) — the size of array a and the number of queries to it. The next line contains n space-separated positive integers a1, a2, ..., an (1 ≤ ai ≤ 109). Next m lines contain descriptions of queries, one per line. The j-th of these lines contains the description of the j-th query as two space-separated integers lj and rj (1 ≤ lj ≤ rj ≤ n).

Output

In m lines print m integers — the answers to the queries. The j-th line should contain the answer to the j-th query.

Examples

Input

7 2
3 1 2 2 3 3 7
1 7
3 4


Output

3
1
"""

def count_exact_occurrences(n, m, a, queries):
    # Helper class for query processing
    class Query:
        def __init__(self, l, r, i):
            self.lb = (l - 1) // z
            self.l = l
            self.r = r
            self.ind = i

        def __lt__(self, other):
            return self.lb < other.lb or (self.lb == other.lb and self.r < other.r)

    # Initialize variables
    z = int(n ** 0.5)
    query_list = [Query(l, r, i) for i, (l, r) in enumerate(queries)]
    query_list.sort()
    
    d = [0] * (n + 2)
    l = 1
    r = 0
    ans = 0
    fans = [0] * m
    
    # Process each query
    for q in query_list:
        while r < q.r:
            r += 1
            if d[a[r - 1]] == a[r - 1]:
                ans -= 1
            d[a[r - 1]] += 1
            if d[a[r - 1]] == a[r - 1]:
                ans += 1
        
        while l > q.l:
            l -= 1
            if d[a[l - 1]] == a[l - 1]:
                ans -= 1
            d[a[l - 1]] += 1
            if d[a[l - 1]] == a[l - 1]:
                ans += 1
        
        while l < q.l:
            if d[a[l - 1]] == a[l - 1]:
                ans -= 1
            d[a[l - 1]] -= 1
            if d[a[l - 1]] == a[l - 1]:
                ans += 1
            l += 1
        
        while r > q.r:
            if d[a[r - 1]] == a[r - 1]:
                ans -= 1
            d[a[r - 1]] -= 1
            if d[a[r - 1]] == a[r - 1]:
                ans += 1
            r -= 1
        
        fans[q.ind] = ans
    
    return fans