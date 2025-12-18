"""
QUESTION:
The King of Byteland wants to grow his territory by conquering $\mbox{K}$ other countries. To prepare his $\begin{array}{c}4\end{array}$ heirs for the future, he decides they must work together to capture each country. 

The King has an army, $\mbox{A}$, of $N$ battalions; the $i^{\mbox{th}}$ battalion has $A_i$ soldiers. For each battle, the heirs get a detachment of soldiers to share but will fight amongst themselves and lose the battle if they don't each command the same number of soldiers (i.e.: the detachment must be divisible by $\begin{array}{c}4\end{array}$). If given a detachment of size $\mbox{0}$, the heirs will fight alone without any help.

The battalions chosen for battle must be selected in the following way:

A subsequence of $\mbox{K}$ battalions must be selected (from the $N$ battalions in army $\mbox{A}$). 
The $j^{th}$ battle will have a squad of soldiers from the $j^{th}$ selected battalion such that its size is divisible by $\begin{array}{c}4\end{array}$. 

The soldiers within a battalion have unique strengths. For a battalion of size $5$, the detachment of soldiers $\{0,1,2,3\}$ is different from the detachment of soldiers $\{0,1,2,4\}$

The King tasks you with finding the number of ways of selecting $\mbox{K}$ detachments of battalions to capture $\mbox{K}$ countries using the criterion above. As this number may be quite large, print the answer modulo $10^9+7$.

Input Format

The first line contains two space-separated integers, $N$ (the number of battalions in the King's army) and $\mbox{K}$ (the number of countries to conquer), respectively.

The second line contains $N$ space-separated integers describing the King's army, $\mbox{A}$, where the $i^{\mbox{th}}$ integer denotes the number of soldiers in the $i^{\mbox{th}}$ battalion ($A_i$). 

Constraints

$1\leq N\leq10^4$
$1\leq K\leq min(100,N)$
$1\leq A_i\leq10^9$
$1\leq A_i\leq10^3$ holds for test cases worth at least $30\%$ of the problem's score.

Output Format

Print the number of ways of selecting the $\mbox{K}$ detachments of battalions modulo $10^9+7$.

Sample Input
3 2
3 4 5

Sample Output
20

Explanation

First, we must find the ways of selecting $2$ of the army's $3$ battalions; then we must find all the ways of selecting detachments for each choice of battalion. 

Battalions $\{A_{0},A_{1}\}$: 

$\boldsymbol{A_0}$ has $3$ soldiers, so the only option is an empty detachment ($\{\}$). 

$\boldsymbol{A_1}$ has $\begin{array}{c}4\end{array}$ soldiers, giving us $2$ detachment options ($\{\}$ and $\{0,1,2,3\}$). 

So for this subset of battalions, we get $1\times2=2$ possible detachments.

Battalions $\{A_{0},A_{2}\}$: 

$\boldsymbol{A_0}$ has $3$ soldiers, so the only option is an empty detachment ($\{\}$). 

$\boldsymbol{A_{2}}$ has $5$ soldiers, giving us $\boldsymbol{6}$ detachment options ($\{\}$, $\{0,1,2,3\}$, $\{0,1,2,4\}$, $\{1,2,3,4\}$, $\{0,1,3,4\}$, $\{0,2,3,4\}$).
So for this subset of battalions, we get $1\times6=6$ possible detachments.

Battalions $\{A_{1},A_{2}\}$: 

$\boldsymbol{A_1}$ has $\begin{array}{c}A\end{array}$ soldiers, giving us $2$ detachment options ($\{\}$ and $\{0,1,2,3\}$). 

$\boldsymbol{A_{2}}$ has $5$ soldiers, giving us $\boldsymbol{6}$ detachment options ($\{\}$, $\{0,1,2,3\}$, $\{0,1,2,4\}$, $\{1,2,3,4\}$, $\{0,1,3,4\}$, $\{0,2,3,4\}$). 

So for this subset of battalions, we get $2\times6=12$ possible detachments.

In total, we have $2+6+12=20$ ways to choose detachments, so we print $20\%(10^9+7)$, which is $\textbf{20}$.
"""

import math

MOD = int(1000000000.0 + 7)
ans = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def S_(n, k):
    def cnk(n, k):
        return int(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
    return sum((cnk(n, i) for i in range(k, n + 1, 4))) % MOD

def S(n, k=0):
    if n < 5:
        return sum(ans[n][k::4])
    r = pow(2, n - 2, MOD) - pow(2, n // 2, MOD)
    if n & 1:
        r = (r + pow(2, (n - 3) // 2, MOD) * sum(ans[3][(k - (n - 3) // 2) % 4::4])) % MOD
    else:
        r = (r + pow(2, (n - 3) // 2, MOD) * sum(ans[4][(k - (n - 3) // 2) % 4::4])) % MOD
    return int(r)

def count_ways_to_conquer(N, K, A):
    det = [S(i) for i in A]
    mem = [[float('+inf')] * (i + 1) for i in range(N + 1)]
    mem[0][0] = 1
    
    for i in range(1, N + 1):
        mem[i][1] = sum(det[:i]) % MOD
        mem[i][i] = mem[i - 1][i - 1] * det[i - 1] % MOD
    
    for i in range(3, N + 1):
        for j in range(2, min(i, K + 1)):
            mem[i][j] = (mem[i - 1][j] + mem[i - 1][j - 1] * det[i - 1]) % MOD
    
    return mem[N][K]