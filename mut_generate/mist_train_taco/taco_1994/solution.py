"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

$N$ integers $A_{1}, A_{2}, \ldots, A_{N}$ are placed in a circle in such a way that for each valid $i$, $A_{i}$ and $A_{i+1}$ are adjacent, and $A_{1}$ and $A_{N}$ are also adjacent.

We want to repeat the following operation exactly $N-1$ times (until only one number remains):
Select two adjacent numbers. Let's denote them by $a$ and $b$.
Score $a+b$ penalty points.
Erase both $a$ and $b$ from the circle and insert $a+b$ in the space between them.

What is the minimum number of penalty points we can score?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $a_{1}, a_{2}, \ldots, a_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the minimum number of penalty points.

------  Constraints  ------
$1 ≤ T ≤ 10$
$2 ≤ N ≤ 400$
$1 ≤ a_{i} ≤ 10^{9}$ for each valid $i$

------  Subtasks ------
Subtask #1 (10 points):
$2 ≤ N ≤ 10$
$a_{i} ≤ 10$ for each valid $i$

Subtask #2 (10 points):
$2 ≤ N ≤ 25$
$a_{1}, a_{2}, \ldots, a_{N}$ are distinct powers of $2$ (including $1$)

Subtask #3 (10 points): $2 ≤ N ≤ 100$

Subtask #4 (70 points): original constraints

----- Sample Input 1 ------ 
1
3
10 10 1
----- Sample Output 1 ------ 
32
----- explanation 1 ------ 
- $[10,10,1] \rightarrow [10, 11]$, penalty:  $11$
- $[10,11] \rightarrow [21]$, penalty:  $21$
- Total penalty: $11+21=32$
"""

def minimum_penalty_points(tone, n):
    if n == 2:
        return sum(tone)
    
    n = n * 2
    tone = tone + tone
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    sk = [[None] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][i] = 0
        sk[i][i] = i
    
    sm = [tone[0]]
    for i in range(1, n):
        sm.append(sm[i - 1] + tone[i])
    
    for gap in range(1, n // 2):
        for i in range(n - gap):
            j = i + gap
            tmp = sm[j] - (0 if i == 0 else sm[i - 1])
            i1, j1 = sk[i][j - 1], sk[i + 1][j] + 1
            for k in range(i1, j1):
                if dp[i][j] > dp[i][k] + dp[k + 1][j] + tmp:
                    dp[i][j], sk[i][j] = dp[i][k] + dp[k + 1][j] + tmp, k
    
    return min([dp[i][i + n // 2 - 1] for i in range(n // 2)])