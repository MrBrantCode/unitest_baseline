"""
QUESTION:
Nobuo-kun and Shizuo-kun are playing a game of competing for territories on a rectangular island. As shown in Fig. 1 below, the entire island is made up of square compartments divided in a grid pattern, and the profits and losses resulting from these are indicated by integers.

<image>



In this game, move one piece to determine the boundaries of the territory. At the beginning of the game, the piece is at the northwestern end of the island (Fig. ①). The trajectory of the piece when moving this piece to the southeastern end of the island becomes the boundary of the territory. The two players move the pieces alternately. Pieces can only be moved to the grid point next to the south or the grid point next to the east (Fig. 2). When the piece reaches the edge of the island, move it in the south or east direction. The game is over when the piece reaches the southeastern end.

The area on the northeast side of the boundary after the game is the area of ​​the first player, and the area on the southwest side is the area of ​​the second player (Fig. ③). The sum of the profits and losses generated from the parcels contained within each player's territory is that player's core. Both of them are quite accustomed to the game and move the pieces accurately so that the value obtained by subtracting the opponent's score from their own score is the largest in the end.




Create a program that calculates the outcome at the end of the game given the size of the island and the gains and losses that result from each parcel. The result is the absolute value of the difference between the scores of Nobuo-kun and Shizuo-kun.



Input

The input is given in the following format.


W H
s1,1 s1,2 ... s1, W
s2,1 s2,2 ... s2, W
::
sH, 1 sH, 2 ... sH, W


The first line gives the number of east-west and north-south sections contained in the island W, H (1 ≤ W, H ≤ 1000). The following row H is given the gains and losses si, j (-1000 ≤ si, j ≤ 1000) that arise from the compartments in row i and column j. However, the direction in which the value of i increases is south, and the direction in which the value of j increases is east.

Output

The absolute value of the difference between the scores of Nobuo-kun and Shizuo-kun is output in one line.

Examples

Input

2 1
-2 1


Output

1


Input

2 2
2 -3
3 -1


Output

3


Input

5 4
5 3 2 -5 2
2 -4 2 8 -4
2 3 -7 6 7
3 -4 10 -3 -3


Output

5
"""

def calculate_territory_difference(W, H, S):
    """
    Calculate the absolute value of the difference between the scores of Nobuo-kun and Shizuo-kun
    after they play the territory game on a rectangular island.

    Parameters:
    W (int): The number of columns (width) of the island.
    H (int): The number of rows (height) of the island.
    S (list of list of int): A 2D list representing the gains and losses for each compartment on the island.

    Returns:
    int: The absolute value of the difference between the scores of Nobuo-kun and Shizuo-kun.
    """
    SW = [[0] * W for _ in range(H)]
    SH = [[0] * W for _ in range(H)]
    
    # Calculate SW
    for i in range(H):
        cnt = 0
        for j in range(W - 1, -1, -1):
            cnt += S[i][j]
            SW[i][j] = cnt
    
    # Calculate SH
    for j in range(W):
        cnt = 0
        for i in range(H - 1, -1, -1):
            cnt += S[i][j]
            SH[i][j] = cnt
    
    memo = {}
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[x, y]
        if x == W or y == H:
            return 0
        if (x + y) % 2 == 0:
            res = max(dfs(x + 1, y) - SH[y][x], dfs(x, y + 1) + SW[y][x])
        else:
            res = min(dfs(x + 1, y) - SH[y][x], dfs(x, y + 1) + SW[y][x])
        memo[x, y] = res
        return res
    
    return abs(dfs(0, 0))