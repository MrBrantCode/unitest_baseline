"""
QUESTION:
There are $n$ segments $[l_i, r_i]$ for $1 \le i \le n$. You should divide all segments into two non-empty groups in such way that there is no pair of segments from different groups which have at least one common point, or say that it's impossible to do it. Each segment should belong to exactly one group.

To optimize testing process you will be given multitest.


-----Input-----

The first line contains one integer $T$ ($1 \le T \le 50000$) — the number of queries. Each query contains description of the set of segments. Queries are independent.

First line of each query contains single integer $n$ ($2 \le n \le 10^5$) — number of segments. It is guaranteed that $\sum{n}$ over all queries does not exceed $10^5$.

The next $n$ lines contains two integers $l_i$, $r_i$ per line ($1 \le l_i \le r_i \le 2 \cdot 10^5$) — the $i$-th segment.


-----Output-----

For each query print $n$ integers $t_1, t_2, \dots, t_n$ ($t_i \in \{1, 2\}$) — for each segment (in the same order as in the input) $t_i$ equals $1$ if the $i$-th segment will belongs to the first group and $2$ otherwise.

If there are multiple answers, you can print any of them. If there is no answer, print $-1$.


-----Example-----
Input
3
2
5 5
2 3
3
3 5
2 3
2 3
3
3 3
4 4
5 5

Output
2 1 
-1
1 1 2 



-----Note-----

In the first query the first and the second segments should be in different groups, but exact numbers don't matter.

In the second query the third segment intersects with the first and the second segments, so they should be in the same group, but then the other group becomes empty, so answer is $-1$.

In the third query we can distribute segments in any way that makes groups non-empty, so any answer of $6$ possible is correct.
"""

def divide_segments(segments):
    n = len(segments)
    if n < 2:
        return -1  # There must be at least two segments to form two non-empty groups

    # Convert segments to include original indices
    indexed_segments = [(l, r, i) for i, (l, r) in enumerate(segments)]
    
    # Sort segments based on the right endpoint
    indexed_segments.sort(key=lambda x: x[1])
    
    # Find the index where the division can happen
    mn = indexed_segments[-1][0]
    index = -1
    for i in range(n - 2, -1, -1):
        if indexed_segments[i][1] >= mn:
            mn = min(mn, indexed_segments[i][0])
        else:
            index = i
            break
    
    if index == -1:
        return -1  # No valid division point found
    
    # Assign groups based on the division point
    result = [0] * n
    for i in range(n):
        if i <= index:
            result[indexed_segments[i][2]] = 1
        else:
            result[indexed_segments[i][2]] = 2
    
    return result