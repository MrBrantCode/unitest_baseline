"""
QUESTION:
Given a permutation P of size N, an array A of size N can be generated using the following method:

If P_{i}> P_{j} for all (1 ≤ j < i), set A_{i}=0;
Otherwise, set A_{i} = max(j) where (1 ≤ j < i) and (P_{j} > P_{i}).

Unfortunately, we lost the permutation P and some elements of the array A.  
The lost elements of the array A are denoted as A_{i} = -1. These elements can be replaced with any non-negative integer.

Given an array A with some lost elements, check whether there exists a permutation P, such that, we can obtain the array A from P using the above method.  
If at least one such permutations exist, print the lexicographically smallest permutation.  
If no such permutation exists, print -1 instead.

Note:
A permutation of size N contains each element from 1 to N exactly once.
Permutation X is said to be lexicographically smaller than permutation Y if:
- X_{i} < Y_{i};
- X_{j} = Y_{j} for all (1≤ j < i).

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains an integer N — the size of A.
- The next line contains N space-separated integers: A_{1},A_{2},\ldots ,A_{N}. 

------ Output Format ------ 

For each test case, output on a new line:
- If at least one such permutations exist, print the lexicographically smallest permutation.  
- If no such permutation exists, print -1 instead.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N ≤ 2\cdot 10^{5}$
$-1 ≤ A_{i} < N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
4
5
0 0 2 3 0
5
0 0 1 2 4
2
1 -1
4
-1 -1 -1 -1
----- Sample Output 1 ------ 
1 4 3 2 5
-1
-1
1 2 3 4

----- explanation 1 ------ 
Test case$1$: There are $3$ permutations which meet the condition $\{[1,4,3,2,5],[2,4,3,1,5],[3,4,2,1,5]\}$.  
The lexicographically smallest permutation is $[1,4,3,2,5]$. The array $A$ is obtained as:
- $A_{1}$: $A_{1} = 0$ as there exists no $j < 1$ for which $P_{i}< P_{j}$.
- $A_{2}$: Since $P_{2} > P_{1}$, $A_{2} = 0$.
- $A_{3}$: We set $A_{3}$ as the maximum $j$ such that $j< 3$ and $P_{j} > P_{3}$. Thus, $A_{3} = j = 2$.
- $A_{4}$: We set $A_{4}$ as the maximum $j$ such that $j< 4$ and $P_{j} > P_{4}$. Thus, $A_{3} = j = 3$.
- $A_{5}$: Since $P_{5}$ is greater than $P_{1}, P_{2}, P_{3},$ and $P_{4}$, $A_{5} = 0$.

Test case $2$: No permutation meets the condition.

Test case $3$: No permutation meets the condition.

Test case $4$: Since all elements of the array are missing, we can assume the elements.  
Consider the array $[0, 0, 0, 0]$. The lexicographically smallest permutation using which the array $A$ can be generated is $[1, 2, 3, 4]$.
"""

import heapq

def find_lexicographically_smallest_permutation(n, a):
    a = [-1] + a  # Adjusting the array to be 1-indexed
    g = [[] for _ in range(n + 1)]
    found = True
    pts = []
    indegs = [0] * (n + 1)
    edges = 0

    for i in range(1, n + 1):
        if a[i] == -1:
            continue
        elif a[i] >= i:
            found = False
            break
        elif a[i] != 0:
            g[i].append(a[i])
            indegs[a[i]] += 1
            edges += 1
            while pts and pts[-1] > a[i]:
                j = pts.pop()
                g[j].append(i)
                indegs[i] += 1
                edges += 1
        pts.append(i)

    if not found:
        return -1

    hq = [i for i in range(1, n + 1) if indegs[i] == 0]
    res = [0] * (n + 1)
    p = 1

    while hq:
        cur = heapq.heappop(hq)
        res[cur] = p
        p += 1
        for nxt in g[cur]:
            indegs[nxt] -= 1
            edges -= 1
            if indegs[nxt] == 0:
                heapq.heappush(hq, nxt)

    if edges > 0:
        return -1

    return res[1:]