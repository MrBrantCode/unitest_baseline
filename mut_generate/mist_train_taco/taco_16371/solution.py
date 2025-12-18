"""
QUESTION:
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.
Note:
The initial and the target position coordinates of Knight have been given according to 1-base indexing.
 
Example 1:
Input:
N=6
knightPos[ ] = {4, 5}
targetPos[ ] = {1, 1}
Output:
3
Explanation:
Knight takes 3 step to reach from 
(4, 5) to (1, 1):
(4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the initial position of Knight (KnightPos), the target position of Knight (TargetPos), and the size of the chessboard (N) as input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position or return -1 if its not possible.
 
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(N^{2}).
 
Constraints:
1 <= N <= 1000
1 <= Knight_pos(X, Y), Targer_pos(X, Y) <= N
"""

def min_steps_to_reach_target(knight_pos, target_pos, N):
    # Initialize the visited array
    vis = [[-1] * (N + 1) for _ in range(N + 1)]
    
    # If the initial position is the same as the target position
    if knight_pos == target_pos:
        return 0
    
    # Possible moves for a knight
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, -2), (-1, 2)
    ]
    
    # Queue for BFS
    q = [(knight_pos[0], knight_pos[1], 0)]
    vis[knight_pos[0]][knight_pos[1]] = 0
    
    # BFS loop
    while q:
        x, y, step = q.pop(0)
        for dx, dy in moves:
            r = x + dx
            c = y + dy
            if (r, c) == target_pos:
                return step + 1
            if 1 <= r <= N and 1 <= c <= N and vis[r][c] == -1:
                q.append((r, c, step + 1))
                vis[r][c] = step + 1
    
    # If target is not reachable
    return -1