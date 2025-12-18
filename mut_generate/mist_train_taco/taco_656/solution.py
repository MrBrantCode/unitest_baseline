"""
QUESTION:
Timur's grandfather gifted him a chessboard to practice his chess skills. This chessboard is a grid $a$ with $n$ rows and $m$ columns with each cell having a non-negative integer written on it.

Timur's challenge is to place a bishop on the board such that the sum of all cells attacked by the bishop is maximal. The bishop attacks in all directions diagonally, and there is no limit to the distance which the bishop can attack. Note that the cell on which the bishop is placed is also considered attacked. Help him find the maximal sum he can get.


-----Input-----

The first line of the input contains a single integer $t$ ($1 \le t \le 1000$) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers $n$ and $m$ ($1 \le n \le 200$, $1 \leq m \leq 200$).

The following $n$ lines contain $m$ integers each, the $j$-th element of the $i$-th line $a_{ij}$ is the number written in the $j$-th cell of the $i$-th row $(0\leq a_{ij} \leq 10^6)$

It is guaranteed that the sum of $n\cdot m$ over all test cases does not exceed $4\cdot10^4$.


-----Output-----

For each test case output a single integer, the maximum sum over all possible placements of the bishop.


-----Examples-----

Input
4
4 4
1 2 2 1
2 4 2 4
2 2 3 1
2 4 2 4
2 1
1
0
3 3
1 1 1
1 1 1
1 1 1
3 3
0 1 1
1 0 1
1 1 0
Output
20
1
5
3


-----Note-----

For the first test case here the best sum is achieved by the bishop being in this position:
"""

def max_bishop_attack_sum(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, a = case
        l = [0] * (m + n)
        r = [0] * (m + n)
        
        for i in range(n):
            for j in range(m):
                b = a[i][j]
                l[i - j + m - 1] += b
                r[i + j] += b
        
        max_sum = max((l[i - j + m - 1] + r[i + j] - a[i][j] for i in range(n) for j in range(m)))
        results.append(max_sum)
    
    return results