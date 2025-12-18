"""
QUESTION:
Chef has a sequence $A_{1}, A_{2}, \ldots, A_{N}$. For a positive integer $M$, sequence $B$ is defined as $B = A*M$ that is, appending $A$ exactly $M$ times. For example, If $A = [1, 2]$ and $M = 3$, then $B = A*M = [1, 2, 1, 2, 1, 2]$

You have to help him to find out the minimum value of $M$ such that the length of the longest strictly increasing subsequence is maximum possible.

------ Input: ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------ Output: ------
For each test case, print a single line containing one integer ― the minimum value of $M$.

------ Constraints  ------
$1 ≤ T ≤ 500$
$1 ≤ N ≤ 2*10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
It's guaranteed that the total length of the sequence $A$ in one test file doesn't exceed $2*10^{6}$

----- Sample Input 1 ------ 
3
2
2 1
2
1 2
5
1 3 2 1 2
----- Sample Output 1 ------ 
2
1
2
----- explanation 1 ------ 
In the first test case, Choosing $M = 2$ gives $B = [2, 1, 2, 1]$ which has a longest strictly increasing sequence of length $2$ which is the maximum possible.

In the second test case, Choosing $M = 1$ gives $B  = [1, 2]$ which has a longest strictly increasing sequence of length $2$ which is the maximum possible.
"""

from collections import defaultdict

def find_minimum_M(A, N):
    L = [[]]
    D = defaultdict(int)
    S = set()
    p = 0
    
    for n in A:
        if n in S:
            q = D[n]
        else:
            S.add(n)
            q = len(L)
            L.append([])
            D[n] = q
        L[q].append(p)
        p += 1
    
    SL = list(S)
    SL.sort()
    p = 0
    M = 1
    
    for n in SL:
        q = D[n]
        if len(L[q]) == 1:
            z = L[q][0]
            if z < p:
                M += 1
            p = z
        else:
            v = L[q][-1]
            if v > p:
                k = 0
                while L[q][k] < p:
                    k += 1
                p = L[q][k]
            else:
                M += 1
                p = L[q][0]
    
    return M