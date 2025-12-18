"""
QUESTION:
table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.


       
               
                       -2 (K)
                       -3
                       3
               
               
                       -5
                       -10
                       1
               
               
                       10
                       30
                       -5 (P)
               
       


 

Note:


       The knight's health has no upper bound.
       Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""

def calculate_minimum_initial_health(dungeon):
    row = len(dungeon)
    col = len(dungeon[0])
    dp = [[0 for _ in range(col)] for _ in range(row)]
    
    # Initialize the bottom-right corner
    if dungeon[-1][-1] <= 0:
        dp[-1][-1] = -dungeon[-1][-1] + 1
    else:
        dp[-1][-1] = 1
    
    # Fill the last column
    for r in range(row - 2, -1, -1):
        dp[r][-1] = dp[r + 1][-1] - dungeon[r][-1]
        if dp[r][-1] <= 0:
            dp[r][-1] = 1
    
    # Fill the last row
    for c in range(col - 2, -1, -1):
        dp[-1][c] = dp[-1][c + 1] - dungeon[-1][c]
        if dp[-1][c] <= 0:
            dp[-1][c] = 1
    
    # Fill the rest of the dp table
    for r in range(row - 2, -1, -1):
        for c in range(col - 2, -1, -1):
            dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
            if dp[r][c] <= 0:
                dp[r][c] = 1
    
    return dp[0][0]