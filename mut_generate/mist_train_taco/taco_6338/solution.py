"""
QUESTION:
One day, Wet Shark was given an array $X=\{x_1,x_2,\ldots,x_m\}$. As always, he started playing with its subsequences. 

When you came to know about this habit, you presented him a task of finding all pairs of subsequences, $(A,B)$, which satisfies all of the following constraints. We will represent a pair of subsequence as $A=\{x_{a_1},x_{a_2},...,x_{a_n}\}$ and $B=\{x_{b_1},x_{b_2},...,x_{b_n}\}$ 

$\mbox{A}$ and $\mbox{B}$ must be of same length, i.e., $|A|=|B|$.
$\sum\limits_{i=1}^{n}(x_{a_{i}}+x_{b_{i}})=r$
$\sum\limits_{i=1}^{n}(x_{a_{i}}-x_{b_{i}})=s$

Please help Wet Shark determine how many possible subsequences $\mbox{A}$ and $\mbox{B}$ can exist. Because the number of choices may be big, output your answer modulo $10^9+7=1000000007$. 

Note: 

Two segments are different if there's exists at least one index $\boldsymbol{i}$ such that element $x_i$ is present in exactly one of them.
Both subsequences can overlap each other.
Subsequences do not necessarily have to be distinct

Input Format

The first line consists of 3 space-separated integers $m$, $\textbf{r}$, $\boldsymbol{\mathrm{~S~}}$, where $m$ denotes the length of the original array, $\mbox{X}$, and $\textbf{r}$ and $\boldsymbol{\mathrm{~S~}}$ are as defined above. 

The next line contains $m$ space-separated integers, $x_1,x_2,\ldots,x_m$ , representing the elements of $\mbox{X}$.

Constraints

$1\leq m\leq100$  
$0\leq r,\:\textit{s}\leq2000$  
$1\leq x_i\leq2000$  

Output Format

Output total number of pairs of subsequences, $(A,B)$, satisfying the above conditions. As the number can be large, output it's modulo $10^9+7=1000000007$

Sample Input 0
4 5 3
1 1 1 4

Sample Output 0
3

Explanation 0

For array $X=\{x_1,x_2,x_3,x_4\}=\{1,1,1,4\}$ there are three pairs of subsequences: 

$A=\{x_4\}=\{4\};B=\{x_1\}=\{1\}$
$A=\{x_4\}=\{4\};B=\{x_2\}=\{1\}$
$A=\{x_4\}=\{4\};B=\{x_3\}=\{1\}$
"""

def count_subsequence_pairs(m, r, s, arr):
    mod = 10 ** 9 + 7
    
    if m == 0 or r <= s:
        return 0
    
    if (r - s) % 2 != 0:
        return 0
    
    sumb = (r - s) // 2
    suma = r - sumb

    def get_ways(num):
        dp = [[0] * (num + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for c in arr:
            for i in range(len(dp[0]) - 1, c - 1, -1):
                for j in range(len(dp) - 2, -1, -1):
                    if dp[j][i - c] > 0:
                        dp[j + 1][i] += dp[j][i - c]
        for j in range(len(dp)):
            if dp[j][num] > 0:
                yield (j, dp[j][num])
    
    a = list(get_ways(suma))
    b = list(get_ways(sumb))
    
    res = 0
    for i in a:
        for j in b:
            if i[0] == j[0]:
                res += i[1] * j[1]
    
    return res % mod