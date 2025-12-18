"""
QUESTION:
Read problems statements [Mandarin] , [Bengali] , [Hindi] , [Russian] and [Vietnamese] as well.

Chef's brother Chefu is a competitive programmer. Every day, he practices for ICPC (International Chefs' Programming Contest) by solving problems. Today, Chef challenged his brother to solve a certain problem, promising to bake an apple pie for him if he succeeds. Chefu has successfully solved the problem, but can you solve it? 

You are given an integer sequence $A_{1}, A_{2}, \ldots, A_{N}$. In one move, you must select two adjacent elements of this sequence (i.e. $A_{i}$ and $A_{i+1}$ for some valid $i$) and swap them. Let's call a sequence *orderly* if it contains a contiguous subsequence with length at least $K$ such that all of its elements have identical values. Find the minimum number of moves required to make the given sequence orderly or determine that it is impossible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $K$. 
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \ldots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the minimum required number of moves, or $-1$ if it is impossible to make the sequence orderly.

------  Constraints  ------
$1 ≤ T ≤ 1,000$
$2 ≤ K ≤ N ≤ 300,000$
$1 ≤ A_{i} ≤ 300,000$ for each valid $i$
the sum of $N$ over all test cases does not exceed $10^{6}$

------  Subtasks ------
Subtask #1 (30 points):
$N ≤ 100$
the sum of $N$ over all test cases does not exceed $1,000$

Subtask #2 (70 points): original constraints

----- Sample Input 1 ------ 
2
8 3
1 2 2 1 3 3 2 1
5 3
1 1 2 2 3
----- Sample Output 1 ------ 
3
-1
"""

from collections import Counter, defaultdict

def min_moves_to_orderly_sequence(N, K, A):
    c = Counter(A)
    d = defaultdict(list)
    fl = []
    f = 0
    
    for x, y in c.items():
        if y >= K:
            f = 1
            fl.append(x)
    
    if not f:
        return -1
    
    for i in range(N):
        d[A[i]].append(i)
    
    mdif = float('inf')
    
    for i in fl:
        dif = 0
        if K % 2:
            for j in range(K):
                dif += abs(d[i][j] - d[i][K // 2]) - abs(j - K // 2)
            q = 0
            for j in range(K // 2 + 1, len(d[i]) - K // 2):
                q += d[i][j + K // 2] - d[i][j] - (d[i][j - 1] - d[i][j - 1 - K // 2])
                if q < 0:
                    dif += q
                    q = 0
        else:
            for j in range(K):
                dif += abs(d[i][j] - d[i][K // 2]) - abs(j - K // 2)
            q = 0
            for j in range(K // 2 + 1, len(d[i]) - K // 2 + 1):
                q += d[i][j + K // 2 - 1] - d[i][j] - (d[i][j - 1] - d[i][j - 1 - K // 2]) + d[i][j] - d[i][j - 1]
                if q < 0:
                    dif += q
                    q = 0
        
        mdif = min(dif, mdif)
    
    return mdif