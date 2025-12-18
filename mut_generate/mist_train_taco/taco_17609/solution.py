"""
QUESTION:
In the game of Broken Blocks, the player is allowed to move on m x n blocks i.e. m levels and n stone blocks on each level such that one level is vertically above the previous level (as in a staircase), with some of its stone blocks replaced by wooden blocks.
The player at the start of the game is present on the ground level (which should be considered as level 0 or it can be considered as level -1). The player can start from any of the blocks present on the level 0 and start moving further to next levels. The player can only move to the stone-block just above to the present stone-block or diagonally to the left or to the right. The player cant move on the same level.
If the player steps on any of the wooden block (denoted by -1), he will fall off the board and die as the wood-block will not able to hold players weight. Each of the stone-block has some gold coins present on it (wooden blocks doesnt have any coins on them). If at any point the player cant move to further level due to any reason, the game ends and his present total coin score will be considered.
The players aim is to collect as many gold coins as he can without falling off the board.
 
Example 1:
Input: matrix = {{2,5,6},{-1,3,2},{4,-1,5}}
Output: 14
Explanation: Assume 0-based indexing.The matrix 
is:
2 5 6 (level 0)
-1 3 2 (level 1)
4 -1 5 (lever 2)
The player can collect maximum number of coins 
by moving through:matrix[0][2] + matrix[1][1] 
+ matrix[2][2] = 6 + 3 + 5 = 14 coins.
Example 2:
Input: matrix = {{-1,2,3,4},{5,-1,-1,2},
{4,3,-1,-1}}
Output: 11
Explanation: The matrix is:
-1 2 3 4(level 0)
5 -1 -1 2(level 1)
4 3 -1 1(level 2)
The player can collect maximum number of coins 
by moving through:a[0][1] + a[1][0] + a[2][0] 
= 2 + 5 + 4 = 11 coins.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function MaxGold() which takes matrix as input parameter and returns the maximum number of gold coins.
 
Constraints
1<=n,m<=1000
Expected Time Complexity: O(n*m)
Expected Space Complexity: O(1)
"""

def max_gold_collected(matrix):
    l = len(matrix)
    o = len(matrix[0])
    
    # Edge case: If there's only one level
    if l == 1:
        r = max(matrix[0])
        if r == -1:
            return 0
        return r
    
    # Edge case: If there's only one block per level
    if o == 1:
        p = matrix[0][0]
        if matrix[0][0] == -1:
            return 0
        for h in range(1, l):
            if matrix[h][0] == -1:
                return p
            matrix[h][0] += matrix[h - 1][0]
            p = matrix[h][0]
        return p
    
    # Dynamic programming approach to calculate maximum gold
    for h in range(l - 2, -1, -1):
        for g in range(o):
            m = 0
            if matrix[h][g] == -1:
                continue
            if g == 0 and h + 1 < l and (g + 1 < o):
                m = max(m, matrix[h + 1][g], matrix[h + 1][g + 1])
            elif g == o - 1 and h + 1 < l and (g - 1 < o) and (g - 1 >= 0):
                m = max(m, matrix[h + 1][g], matrix[h + 1][g - 1])
            elif h + 1 < l and g + 1 < o and (g > 0) and (g < o - 1):
                m = max(m, matrix[h + 1][g], matrix[h + 1][g + 1], matrix[h + 1][g - 1])
            matrix[h][g] += m
    
    r = max(matrix[0])
    if r == -1:
        return 0
    return r