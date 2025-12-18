"""
QUESTION:
You have a large rectangular board which is divided into $n \times m$ cells (the board has $n$ rows and $m$ columns). Each cell is either white or black.

You paint each white cell either red or blue. Obviously, the number of different ways to paint them is $2^w$, where $w$ is the number of white cells.

After painting the white cells of the board, you want to place the maximum number of dominoes on it, according to the following rules:

each domino covers two adjacent cells;

each cell is covered by at most one domino;

if a domino is placed horizontally (it covers two adjacent cells in one of the rows), it should cover only red cells;

if a domino is placed vertically (it covers two adjacent cells in one of the columns), it should cover only blue cells.

Let the value of the board be the maximum number of dominoes you can place. Calculate the sum of values of the board over all $2^w$ possible ways to paint it. Since it can be huge, print it modulo $998\,244\,353$.


-----Input-----

The first line contains two integers $n$ and $m$ ($1 \le n, m \le 3 \cdot 10^5$; $nm \le 3 \cdot 10^5$) — the number of rows and columns, respectively.

Then $n$ lines follow, each line contains a string of $m$ characters. The $j$-th character in the $i$-th string is * if the $j$-th cell in the $i$-th row is black; otherwise, that character is o.


-----Output-----

Print one integer — the sum of values of the board over all $2^w$ possible ways to paint it, taken modulo $998\,244\,353$.


-----Examples-----

Input
3 4
**oo
oo*o
**oo
Output
144
Input
3 4
**oo
oo**
**oo
Output
48
Input
2 2
oo
o*
Output
4
Input
1 4
oooo
Output
9


-----Note-----

None
"""

MOD = 998244353

def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % MOD
        a = a * a % MOD
        b //= 2
    return res

def inverse(n):
    return power(n, MOD - 2)

def calculate_board_value(n, m, grid):
    prob = [0, 0]
    for c in range(2, max(n, m) + 1):
        prob.append(prob[-1] + (-1) ** c * inverse(power(2, c)))
        prob[-1] %= MOD
    
    res = 0
    
    # Process rows
    for r in range(n):
        cnt = 0
        for c in range(m):
            if grid[r][c] == 'o':
                cnt += 1
            else:
                cnt = 0
            res += prob[cnt]
            res %= MOD
    
    # Process columns
    for c in range(m):
        cnt = 0
        for r in range(n):
            if grid[r][c] == 'o':
                cnt += 1
            else:
                cnt = 0
            res += prob[cnt]
            res %= MOD
    
    # Multiply by 2 for each white cell
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'o':
                res *= 2
                res %= MOD
    
    return res