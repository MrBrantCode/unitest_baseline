"""
QUESTION:
------Read problems statements in Mandarin chinese
, Russian and Vietnamese as well. ------ 

Maybe Fulu is not so good at writing codes for median elements, but solving problems with queries is really easy for him. Today, he decided to give you one hard problem with queries from his national contest.

You are given two sequences $A$ and $B$, each with length $N$ ($1$-indexed), and $Q$ queries. There are four types of queries:
$1\; l\; r$ — find $\mathrm{max}(A_{l}, A_{l+1}, \dots, A_{r})$
$2\; l\; r$ — increase $A_{l}, A_{l+1}, \dots, A_{r}$ by $B_{l}, B_{l+1}, \dots, B_{r}$, i.e. for each $i$ ($l ≤ i ≤ r$), change $A_{i}$ to $A_{i}+B_{i}$
$3\; l\; r\; x$ — for each $l ≤ i ≤ r$, increase $B_{i}$ by $x$
$4\; l\; r\; x$ — for each $l ≤ i ≤ r$, increase $A_{i}$ by $x$

Can you quickly process the queries?

------  Input ------
The first line of the input contains two space-separated integers $N$ and $Q$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$ denoting the initial sequence $A$.
The third line contains $N$ space-separated integers $B_{1}, B_{2}, \dots, B_{N}$ denoting the initial sequence $B$.
The following $Q$ lines describe queries. Each of these lines starts with an integer $t$ denoting the type of the query. If $1 ≤ t ≤ 2$, it is followed by a space and two space-separated integers $l$ and $r$. If $3 ≤ t ≤ 4$, it is followed by a space and three space-separated integers $l$, $r$ and $x$.

------  Output ------
For each query of the first type, print a single line containing one integer — the maximum element in the subsequence $A_{l..r}$.

------  Constraints ------
$1 ≤ N, Q ≤ 10^{5}$
$|A_{i}| ≤ 10^{9}$ for each valid $i$
$|B_{i}| ≤ 10^{9}$ for each valid $i$
$|x| ≤ 10^{9}$
$1 ≤ l ≤ r ≤ N$

----- Sample Input 1 ------ 
3 6
1 4 2
3 1 2
1 1 3
2 1 3
3 1 1 -2
2 1 3
4 1 2 3
1 1 2
----- Sample Output 1 ------ 
4
9
----- explanation 1 ------ 
Initially, $A = [1, 4, 2]$ and $B = [3, 1, 2]$.
- In the first query, we should find the maximum element of $A$, which is $4$.
- After the second query, $A = [4, 5, 4]$.
- After the third query, $B = [1, 1, 2]$.
- After the fourth query, $A = [5, 6, 6]$.
- After the fifth query, $A = [8, 9, 6]$.
- In the sixth query, we should find the maximum of $A_{1}$ and $A_{2}$, which is $9$.
"""

import numpy as np

def process_queries(n, q, A, B, queries):
    results = []
    a = np.array(A)
    b = np.array(B)
    
    for query in queries:
        if query[0] == 1:
            results.append(np.amax(a[query[1] - 1:query[2]]))
        elif query[0] == 2:
            a[query[1] - 1:query[2]] += b[query[1] - 1:query[2]]
        elif query[0] == 3:
            b[query[1] - 1:query[2]] += query[3]
        elif query[0] == 4:
            a[query[1] - 1:query[2]] += query[3]
    
    return results