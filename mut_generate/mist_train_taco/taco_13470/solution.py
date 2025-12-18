"""
QUESTION:
Baby Ehab has a piece of Cut and Stick with an array a of length n written on it. He plans to grab a pair of scissors and do the following to it:

  * pick a range (l, r) and cut out every element a_l, a_{l + 1}, ..., a_r in this range; 
  * stick some of the elements together in the same order they were in the array; 
  * end up with multiple pieces, where every piece contains some of the elements and every element belongs to some piece. 



More formally, he partitions the sequence a_l, a_{l + 1}, ..., a_r into subsequences. He thinks a partitioning is beautiful if for every piece (subsequence) it holds that, if it has length x, then no value occurs strictly more than ⌈ x/2 ⌉ times in it.

He didn't pick a range yet, so he's wondering: for q ranges (l, r), what is the minimum number of pieces he needs to partition the elements a_l, a_{l + 1}, ..., a_r into so that the partitioning is beautiful.

A sequence b is a subsequence of an array a if b can be obtained from a by deleting some (possibly zero) elements. Note that it does not have to be contiguous.

Input

The first line contains two integers n and q (1 ≤ n,q ≤ 3 ⋅ 10^5) — the length of the array a and the number of queries.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_i ≤ n) — the elements of the array a.

Each of the next q lines contains two integers l and r (1 ≤ l ≤ r ≤ n) — the range of this query.

Output

For each query, print the minimum number of subsequences you need to partition this range into so that the partitioning is beautiful. We can prove such partitioning always exists.

Example

Input


6 2
1 3 2 3 3 2
1 6
2 5


Output


1
2

Note

In the first query, you can just put the whole array in one subsequence, since its length is 6, and no value occurs more than 3 times in it.

In the second query, the elements of the query range are [3,2,3,3]. You can't put them all in one subsequence, since its length is 4, and 3 occurs more than 2 times. However, you can partition it into two subsequences: [3] and [2,3,3].
"""

from bisect import bisect, bisect_left
from random import random

def min_beautiful_partitions(n, a, queries):
    # Precompute the positions of each element in the array
    v = [list() for _ in range(n + 1)]
    for i in range(n):
        v[a[i]].append(i)
    
    results = []
    
    for (l, r) in queries:
        l -= 1
        r -= 1
        ans = 1
        s = set()
        
        for _ in range(25):
            idx = int(random() * (r - l + 1)) + l
            if a[idx] in s:
                continue
            s.add(a[idx])
            
            if len(v[a[idx]]) <= (r - l + 2) // 2:
                continue
            
            left = bisect_left(v[a[idx]], l)
            right = bisect(v[a[idx]], r)
            
            if right - left > (r - l + 2) // 2:
                ans = 2 * (right - left) - (r - l + 1)
                break
        
        results.append(ans)
    
    return results