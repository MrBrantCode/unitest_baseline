"""
QUESTION:
Kuro has recently won the "Most intelligent cat ever" contest. The three friends then decided to go to Katie's home to celebrate Kuro's winning. After a big meal, they took a small break then started playing games.

Kuro challenged Katie to create a game with only a white paper, a pencil, a pair of scissors and a lot of arrows (you can assume that the number of arrows is infinite). Immediately, Katie came up with the game called Topological Parity.

The paper is divided into $n$ pieces enumerated from $1$ to $n$. Shiro has painted some pieces with some color. Specifically, the $i$-th piece has color $c_{i}$ where $c_{i} = 0$ defines black color, $c_{i} = 1$ defines white color and $c_{i} = -1$ means that the piece hasn't been colored yet.

The rules of the game is simple. Players must put some arrows between some pairs of different pieces in such a way that for each arrow, the number in the piece it starts from is less than the number of the piece it ends at. Also, two different pieces can only be connected by at most one arrow. After that the players must choose the color ($0$ or $1$) for each of the unpainted pieces. The score of a valid way of putting the arrows and coloring pieces is defined as the number of paths of pieces of alternating colors. For example, $[1 \to 0 \to 1 \to 0]$, $[0 \to 1 \to 0 \to 1]$, $[1]$, $[0]$ are valid paths and will be counted. You can only travel from piece $x$ to piece $y$ if and only if there is an arrow from $x$ to $y$.

But Kuro is not fun yet. He loves parity. Let's call his favorite parity $p$ where $p = 0$ stands for "even" and $p = 1$ stands for "odd". He wants to put the arrows and choose colors in such a way that the score has the parity of $p$.

It seems like there will be so many ways which satisfy Kuro. He wants to count the number of them but this could be a very large number. Let's help him with his problem, but print it modulo $10^{9} + 7$.


-----Input-----

The first line contains two integers $n$ and $p$ ($1 \leq n \leq 50$, $0 \leq p \leq 1$) — the number of pieces and Kuro's wanted parity.

The second line contains $n$ integers $c_{1}, c_{2}, ..., c_{n}$ ($-1 \leq c_{i} \leq 1$) — the colors of the pieces.


-----Output-----

Print a single integer — the number of ways to put the arrows and choose colors so the number of valid paths of alternating colors has the parity of $p$.


-----Examples-----
Input
3 1
-1 0 1

Output
6
Input
2 1
1 0

Output
1
Input
1 1
-1

Output
2


-----Note-----

In the first example, there are $6$ ways to color the pieces and add the arrows, as are shown in the figure below. The scores are $3, 3, 5$ for the first row and $5, 3, 3$ for the second row, both from left to right.

 [Image]
"""

def count_ways_with_parity(n, p, colors):
    mod = 10**9 + 7
    f = [[[[0] * 2 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
    _2 = [0] * (n + 1)
    _2[0] = 1
    
    for i in range(1, n + 1):
        _2[i] = (_2[i - 1] << 1) % mod
    
    f[0][0][0][0] = 1
    
    nums = [0] + colors  # Adjusting for 1-based indexing
    
    if nums[1] != 0:
        f[1][1][0][1] += 1
    if nums[1] != 1:
        f[1][1][1][0] += 1
    
    for i in range(2, n + 1):
        for j in range(2):
            for ob in range(2):
                for ow in range(2):
                    qwq = f[i - 1][j][ob][ow]
                    if nums[i] != 0:
                        if ob:
                            f[i][j][ob][ow] = (f[i][j][ob][ow] + qwq * _2[i - 2]) % mod
                            f[i][j ^ 1][ob][ow | 1] = (f[i][j ^ 1][ob][ow | 1] + qwq * _2[i - 2]) % mod
                        else:
                            f[i][j ^ 1][ob][ow | 1] = (f[i][j ^ 1][ob][ow | 1] + qwq * _2[i - 1]) % mod
                    if nums[i] != 1:
                        if ow:
                            f[i][j][ob][ow] = (f[i][j][ob][ow] + qwq * _2[i - 2]) % mod
                            f[i][j ^ 1][ob | 1][ow] = (f[i][j ^ 1][ob | 1][ow] + qwq * _2[i - 2]) % mod
                        else:
                            f[i][j ^ 1][ob | 1][ow] = (f[i][j ^ 1][ob | 1][ow] + qwq * _2[i - 1]) % mod
    
    ans = 0
    for i in range(2):
        for j in range(2):
            ans = (ans + f[n][p][i][j]) % mod
    
    return ans