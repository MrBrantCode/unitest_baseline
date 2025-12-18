"""
QUESTION:
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.If it cannot reach the target position return -1.
Note:
The initial and the target position co-ordinates of Knight have been given accoring to 1-base indexing.
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
Example 2:
Input:
N=8
knightPos[ ] = {7, 7}
targetPos[ ] = {1, 5}
Output:
4
Explanation:
Knight takes 4 steps to reach from
(7, 7) to (1, 5):
(4, 5) -> (6, 5) -> (5, 3) -> (7, 2) -> (1, 5).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the inital position of Knight (KnightPos), the target position of Knight (TargetPos) and the size of the chess board (N) as an input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position.If it cannot reach the target position return -1.
Expected Time Complexity: O(N^{2}).
Expected Auxiliary Space: O(N^{2}).
Constraints:
1 <= N <= 1000
1 <= Knight_pos(X, Y), Targer_pos(X, Y) <= N
"""

from collections import deque

def min_steps_to_reach_target(N, knight_pos, target_pos):
    # Convert 1-based indexing to 0-based indexing
    kx, ky = knight_pos[0] - 1, knight_pos[1] - 1
    tx, ty = target_pos[0] - 1, target_pos[1] - 1
    
    # If the knight is already at the target position
    if kx == tx and ky == ty:
        return 0
    
    # Possible moves for a knight
    moves = [
        (-1, 2), (-2, 1), (-2, -1), (-1, -2),
        (1, -2), (2, -1), (2, 1), (1, 2)
    ]
    
    # Initialize the visited matrix
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    # Queue for BFS
    queue = deque([(kx, ky)])
    visited[kx][ky] = True
    steps = 0
    
    # BFS loop
    while queue:
        steps += 1
        size = len(queue)
        for _ in range(size):
            cx, cy = queue.popleft()
            for dx, dy in moves:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if nx == tx and ny == ty:
                        return steps
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # If the target cannot be reached
    return -1