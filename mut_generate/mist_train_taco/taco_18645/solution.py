"""
QUESTION:
You are given $n$ dominoes. Each domino has a left and a right cell. Each cell can be colored either black or white. Some cells are already colored, while some aren't yet.

The coloring is said to be valid if and only if it is possible to rearrange the dominoes in some order such that for each $1 \le i \le n$ the color of the right cell of the $i$-th domino is different from the color of the left cell of the $((i mod n)+1)$-st domino.

Note that you can't rotate the dominoes, so the left cell always remains the left cell, and the right cell always remains the right cell.

Count the number of valid ways to color the yet uncolored cells of dominoes. Two ways are considered different if there is a cell that is colored white in one way and black in the other. In particular, colorings BW WB and WB BW different (and both invalid).

As this number can be very big, output it modulo $998\,244\,353$.


-----Input-----

The first line of the input contains a single integer $n$ ($1 \le n \le 10^5$) — the number of dominoes.

The next $n$ lines describe dominoes. Each line contains two characters which represent the left and the right cell. Character B means that the corresponding cell is black, character W means that the corresponding cell is white, and ? means that the cell is yet to be colored.


-----Output-----

Print a single integer — the answer to the problem.


-----Examples-----

Input
1
?W
Output
1
Input
2
??
W?
Output
2
Input
4
BB
??
W?
??
Output
10


-----Note-----

In the first test case, there is only one domino, and we need the color of its right cell to be different from the color of its left cell. There is only one way to achieve this.

In the second test case, there are only $2$ such colorings:

BB WW and WB WB.
"""

MOD = 998244353
MAX = 200005
fact = [1]
for zz in range(1, MAX + 1):
    fact.append(fact[-1] * zz % MOD)

def nCr(n, r):
    num = fact[n]
    den = fact[r] * fact[n - r] % MOD
    return num * pow(den, MOD - 2, MOD) % MOD

def count_valid_colorings(n, dominoes):
    from collections import Counter
    
    cnts = Counter()
    for s in dominoes:
        cnts[s] += 1
    
    wCnt = bCnt = 0
    for (k, v) in cnts.items():
        for i in range(2):
            if k[i] == 'W':
                wCnt += v
            if k[i] == 'B':
                bCnt += v
    
    if wCnt > n or bCnt > n:
        return 0
    
    gap = n - wCnt + n - bCnt
    total = nCr(gap, n - wCnt)
    
    if cnts['WW'] == cnts['BB'] == 0:
        subtract = 0
        minWBCnts = minBWCnts = 0
        for wb in ['W?', '?B', 'WB']:
            minWBCnts += cnts[wb]
        for bw in ['B?', '?W', 'BW']:
            minBWCnts += cnts[bw]
        gap = n - minWBCnts - minBWCnts
        qq = cnts['??']
        for wbCnts in range(1, n):
            bwCnts = n - wbCnts
            if wbCnts < minWBCnts or bwCnts < minBWCnts:
                continue
            assert qq >= wbCnts - minWBCnts
            subtract += nCr(qq, wbCnts - minWBCnts)
            subtract %= MOD
        total = (total - subtract + MOD) % MOD
    
    return total