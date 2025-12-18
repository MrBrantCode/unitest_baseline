"""
QUESTION:
Write a function `get_shortest_path` that takes three parameters: the start position of a knight on a chessboard, the end position, and a list of blocked positions. The function should return a tuple containing the minimum number of steps for the knight to reach the end position from the start position and the total number of such shortest paths. If the destination is not reachable, the function should return (-1, 0). The chessboard size can be variable, from 8x8 up to 100x100. The knight's moves are defined by the standard chess rules. All positions are 0-indexed.
"""

from collections import deque

def get_shortest_path(start_pos, end_pos, blocked, board_dim=8):
    """
    This function calculates the minimum number of steps for a knight to reach the end position from the start position
    and the total number of such shortest paths on a chessboard of variable size.

    Args:
    start_pos (tuple): The start position of the knight.
    end_pos (tuple): The end position of the knight.
    blocked (list): A list of blocked positions on the chessboard.
    board_dim (int): The size of the chessboard. Default is 8.

    Returns:
    tuple: A tuple containing the minimum number of steps and the total number of such shortest paths.
    """
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = deque() 
    visited = [[False for _ in range(board_dim)] for __ in range(board_dim)]
    shortest_path_count = [[0 for _ in range(board_dim)] for __ in range(board_dim)]
    dist = [[-1 for _ in range(board_dim)] for __ in range(board_dim)]

    for block in blocked:
        visited[block[0]][block[1]] = True

    sx, sy, tx, ty = start_pos[0], start_pos[1], end_pos[0], end_pos[1]
    visited[sx][sy] = True
    dist[sx][sy] = 0
    shortest_path_count[sx][sy] = 1
    queue.append((sx, sy))

    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            return dist[tx][ty], shortest_path_count[tx][ty]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < board_dim and 0 <= ny < board_dim and not visited[nx][ny]:
                if dist[nx][ny] == -1 or dist[nx][ny] == dist[x][y] + 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    shortest_path_count[nx][ny] += shortest_path_count[x][y]

    return -1, 0