"""
QUESTION:
You are given an array, $\mbox{A}$, consisting of $N$ integers.

A segment, $[l,r]$, is beautiful if and only if the bitwise AND of all numbers in $\mbox{A}$ with indices in the inclusive range of $[l,r]$ is not greater than $\mbox{X}$. In other words, segment $[l,r]$ is beautiful if $(A_l\land A_{l+1}\land\ldots\land A_r)\leq X$.

You must answer $\mbox{Q}$ queries. Each query, $Q_j$, consists of $3$ integers: $I_j$, $R_j$, and $X_j$. The answer for each $Q_j$ is the number of beautiful segments $[l,r]$ such that $L_j\leq l\leq r\leq R_j$ and $X=X_j$.

Input Format

The first line contains two space-separated integers, $N$ (the number of integers in $\mbox{A}$) and $\mbox{Q}$ (the number of queries).

The second line contains $N$ space-separated integers, where the $i^{\mbox{th}}$ integer denotes the $i^{\mbox{th}}$ element of array $\mbox{A}$.

Each line $j$ of the $\mbox{Q}$ subsequent lines contains $3$ space-separated integers, $I_j$, $R_j$, and $X_j$, respectively, describing query $Q_j$.

Constraints

$1\leq N\leq4\times10^4$
$1\leq Q\leq10^5$
$1\leq L_j\leq R_j\leq N$
$0\leq X_j\leq2^{17}$
$0\leq A_i<2^{17}$
$1\leq N,Q\leq2000$ holds for test cases worth at least $\textbf{10\%}$ of the problem's score.
$0\leq A_i<2^{11}$ holds for test cases worth at least $\textbf{40\%}$ of the problem's score. 

Output Format

Print $\mbox{Q}$ lines, where the $j^{th}$ line contains the number of beautiful segments for query $Q_j$.

Sample Input
5 3
1 2 7 3 4
1 5 3
2 4 6
3 5 2

Sample Output
13
5
2

Explanation

The beautiful segments for all queries are listed below.

Query 0: The beautiful segments are $[1,\textbf{1}],[\textbf{1},\textbf{2}],[\textbf{1},\textbf{3}],[\textbf{1},\textbf{4}],[\textbf{1},\textbf{5}],[\textbf{2},\textbf{2}],[\textbf{2},\textbf{3}],[\textbf{2},\textbf{4}],[\textbf{2},\textbf{5}],[\textbf{3},\textbf{4}],[\textbf{3},\textbf{5}],[\textbf{4},\textbf{4}],[\textbf{4},\textbf{5}],$.

Query 1: The beautiful segments are $[2,2],[2,3],[2,4],[3,4],[4,4]$.

Query 2: The beautiful segments are $[3,5],[4,5]$.
"""

def count_beautiful_segments(A, queries):
    from itertools import product

    class RangeQuery(object):
        def __init__(self, items, fn):
            self._rq = rq = {(i, 0): item for (i, item) in enumerate(items)}
            self._fn = fn
            n = len(items)
            for (step, i) in product(range(1, n.bit_length()), range(n)):
                j = i + 2 ** (step - 1)
                if j < n:
                    rq[i, step] = fn(rq[i, step - 1], rq[j, step - 1])
                else:
                    rq[i, step] = rq[i, step - 1]

        def query(self, start, stop):
            j = (stop - start).bit_length() - 1
            x = self._rq[start, j]
            y = self._rq[stop - 2 ** j, j]
            return self._fn(x, y)

    def split_segment(start, end, x):
        prev_under = True
        splits = []
        this_under = False
        for i in range(start, end + 1):
            this_under = A[i] <= x
            if this_under != prev_under:
                splits.append(i - int(this_under))
                prev_under = this_under
        if not this_under:
            splits.append(end)
        parts = [[splits[i], splits[i + 1]] for i in range(0, len(splits) - 1, 2)]
        return parts

    rqmax = RangeQuery(A, max)
    results = []

    for (l, r, x) in queries:
        ugly = 0
        segcount = int((r - l + 1) * (r - l + 2) / 2)
        if rqmax.query(l - 1, r) <= x:
            results.append(segcount)
            continue
        splits = split_segment(l - 1, r - 1, x)
        for (sl, sr) in splits:
            if sl == sr:
                ugly += 1
                continue
            for li in range(sl, sr + 1):
                result = A[li]
                for ri in range(li, sr + 1):
                    result &= A[ri]
                    if result > x:
                        ugly += 1
                    else:
                        break
        results.append(segcount - ugly)

    return results