"""
QUESTION:
This year $p$ footballers and $q$ cricketers have been invited to participate in IPL (Indian Programming League) as guests. You have to accommodate them in $r$ rooms such that-
- No room may remain empty.
- A room may contain either only footballers or only cricketers, not both.
- No cricketers are allowed to stay alone in a room.
Find the number of ways to place the players. Note though, that all the rooms are identical. But each of the cricketers and footballers are unique. 
Since the number of ways can be very large, print the answer modulo $998,244,353$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $p$, $q$ and $r$ denoting the number of footballers, cricketers and rooms.

-----Output-----
For each test case, output the number of ways to place the players modulo $998,244,353$.

-----Constraints-----
- $1 \le T \le 100$
- $1 \le p, q, r \le 100$

-----Example Input-----
4
2 1 4
2 4 4
2 5 4
2 8 4

-----Example Output-----
0
3
10
609

-----Explanation-----
Example case 2: Three possible ways are:
- {Footballer 1}, {Footballer 2}, {Cricketer 1, Cricketer 2}, {Cricketer 3, Cricketer 4}
- {Footballer 1}, {Footballer 2}, {Cricketer 1, Cricketer 3}, {Cricketer 2, Cricketer 4}
- {Footballer 1}, {Footballer 2}, {Cricketer 1, Cricketer 4}, {Cricketer 2, Cricketer 3}    
Please note that the rooms are identical.
"""

def calculate_ipl_accommodation_ways(p: int, q: int, r: int, MOD: int = 998244353) -> int:
    fball = [[0] * 101 for _ in range(101)]
    cric = [[0] * 101 for _ in range(101)]

    def calSNum(n, r):
        if n == r or r == 1:
            fball[r][n] = 1
            return
        if n > 0 and r > 0 and (n > r):
            fball[r][n] = (fball[r - 1][n - 1] % MOD + r * fball[r][n - 1] % MOD) % MOD
            return
        fball[r][n] = 0

    def calASNum(n, r):
        if n == 0 and r == 0:
            cric[r][n] = 0
            return
        if n >= 2 and r == 1:
            cric[r][n] = 1
            return
        if r > 0 and n > 0 and (n >= 2 * r):
            cric[r][n] = (r * cric[r][n - 1] % MOD + (n - 1) * cric[r - 1][n - 2] % MOD) % MOD
            return
        cric[r][n] = 0

    def preCompute():
        for r in range(1, 101):
            for n in range(1, 101):
                calSNum(n, r)
                calASNum(n, r)

    preCompute()
    ans = 0
    if p + q // 2 >= r:
        minv = min(p, r)
        for i in range(1, minv + 1):
            if r - i <= q // 2:
                ans = (ans + fball[i][p] * cric[r - i][q] % MOD) % MOD
    return ans