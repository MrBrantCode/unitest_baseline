"""
QUESTION:
You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

d	h	w
1	1	1
1	1	2
1	1	3
1	1	4

Using these blocks, you want to make a wall of height $n$ and width $m$. Features of the wall are: 

- The wall should not have any holes in it. 

- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks. 

- The bricks must be laid horizontally.   

How many ways can the wall be built?

Example  

$n=2$ 

$m=3$  

The height is $2$ and the width is $3$.  Here are some configurations:  

These are not all of the valid permutations.  There are $\mbox{9}$ valid permutations in all.  

Function Description  

Complete the legoBlocks function in the editor below.  

legoBlocks has the following parameter(s):

int n: the height of the wall  
int m: the width of the wall   

Returns 

- int: the number of valid wall formations modulo $(10^9+7)$  

Input Format

The first line contains the number of test cases $\boldsymbol{\boldsymbol{t}}$.  

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains two space-separated integers $n$ and $m$.  

Constraints

$1\leq t\leq100$ 

$1\leq n,m\leq1000$  

Sample Input
STDIN   Function
-----   --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4

Sample Output
3  
7  
9  
3375

Explanation

For the first case, we can have:  

$3\:\:\:\text{mod}\:(10^9+7)=3$  

For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus, the number of ways is $2\times2\times2-1=7$ and $7\:\:\:\text{mod}\:(10^9+7)=7$.
"""

def legoBlocks(n, m):
    MAX = 1000000007
    
    # Helper function to calculate levels
    def calcLevels(levels, N, M):
        levels[1][0] = 1
        p = 1
        while p < M:
            i = 1
            while i <= 4 and p - i >= 0:
                levels[1][p] = (levels[1][p] + levels[1][p - i]) % MAX
                i += 1
            p += 1
        n = 2
        while n < N:
            p = 1
            while p < M:
                levels[n][p] = levels[n - 1][p] * levels[1][p] % MAX
                p += 1
            n += 1
    
    # Helper function to get dynamic programming result
    def getDP(dp, levels, N, M):
        if dp[N][M] != 0:
            return dp[N][M]
        curTmp = levels[N][M]
        p = 1
        while p < M:
            if dp[N][p] == 0:
                curTmpLow = levels[N][p]
                q = 1
                while q < p:
                    curTmpLow = (curTmpLow - dp[N][q] * levels[N][p - q]) % MAX
                    q += 1
                dp[N][p] = curTmpLow
            curTmp = (curTmp - dp[N][p] * levels[N][M - p]) % MAX
            p += 1
        dp[N][M] = curTmp
        return dp[N][M]
    
    # Initialize levels and dp arrays
    levels = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Calculate levels
    calcLevels(levels, n + 1, m + 1)
    
    # Initialize dp array for base cases
    for p in range(n + 1):
        dp[p][1] = 1
    for p in range(m + 1):
        dp[1][p] = levels[1][p]
    
    # Get the result using dynamic programming
    result = getDP(dp, levels, n, m)
    
    return result