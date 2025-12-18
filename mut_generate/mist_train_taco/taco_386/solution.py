"""
QUESTION:
It is well-known that the elephants are afraid of mouses. The Little Elephant from the Zoo of Lviv is not an exception.

The Little Elephant is on a board A of n rows and m columns (0-based numeration). At the beginning he is in cell with coordinates (0; 0) and he wants to go to cell with coordinates (n-1; m-1). From cell (x; y) Little Elephant can go either to (x+1; y) or (x; y+1).

Each cell of the board contains either 1 or 0. If A[i][j] = 1, then there is a single mouse in cell (i; j). Mouse at cell (i; j) scared Little Elephants if and only if during the path there was at least one such cell (x; y) (which belongs to that path) and |i-x| + |j-y| <= 1.

Little Elephant wants to find some correct path from (0; 0) to (n-1; m-1) such that the number of mouses that have scared the Little Elephant is minimal possible. Print that number.

-----Input-----
First line contains single integer T - the number of test cases. Then T test cases follow. First line of each test case contain pair of integers n and m - the size of the board. Next n lines contain n strings, each of size m and consisted of digits 0 and 1.

-----Output-----
In T lines print T integer - the answers for the corresponding test.

-----Constraints-----
1 <= T <= 50
2 <= n, m <= 100

-----Example-----
Input:
2
3 9
001000001
111111010
100100100
7 9
010101110
110110111
010011111
100100000
000010100
011011000
000100101

Output:
9
10

-----Explanation-----
Example case 1: 
The optimized path is: (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (0, 4) -> (0, 5) -> (0, 6) -> (0, 7) -> (0, 8) -> (1, 8) -> (2, 8). The mouses that scared the Little Elephant are at the following cells: (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 7), (0, 2), (0, 8).

Example case 2: 
The optimized path is: (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3) -> (4, 3) -> (4, 4) -> (5, 4) -> (5, 5) -> (6, 5) -> (6, 6) -> (6, 7) -> (6, 8). The 10 mouses that scared the Little Elephant are at the following cells: (0, 1), (1, 0), (1, 1), (2, 1), (3, 3), (4, 4), (5, 4), (5, 5), (6, 6), (6, 8).
"""

from collections import defaultdict
from itertools import product

def min_scared_mice(board, n, m):
    shadow = [[0 for _ in range(m)] for _ in range(n)]
    for (i, j) in product(range(n), range(m)):
        if board[i][j] == 1:
            if i > 0:
                shadow[i - 1][j] += 1
            if j > 0:
                shadow[i][j - 1] += 1
            if i < n - 1:
                shadow[i + 1][j] += 1
            if j < m - 1:
                shadow[i][j + 1] += 1
    
    dp = defaultdict(int)
    dp[0, 0, 0] = dp[0, 0, 1] = shadow[0][0] - board[0][0]
    
    for i in range(1, m):
        dp[0, i, 0] = dp[0, i, 1] = shadow[0][i] - board[0][i] + dp[0, i - 1, 0]
    
    for i in range(1, n):
        dp[i, 0, 0] = dp[i, 0, 1] = shadow[i][0] - board[i][0] + dp[i - 1, 0, 1]
    
    for (i, j) in product(range(1, n), range(1, m)):
        a = shadow[i][j] - board[i][j]
        b = a
        a += min(dp[i, j - 1, 0], dp[i, j - 1, 1] - board[i - 1][j])
        b += min(dp[i - 1, j, 1], dp[i - 1, j, 0] - board[i][j - 1])
        dp[i, j, 0] = a
        dp[i, j, 1] = b
    
    return min(dp[n - 1, m - 1, 0], dp[n - 1, m - 1, 1]) + board[0][0] + board[n - 1][m - 1]