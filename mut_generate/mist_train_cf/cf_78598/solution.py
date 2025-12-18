"""
QUESTION:
Design a function `knight_moves(src, dest, n)` that calculates the shortest path for a knight to move from position `src` to `dest` on an `n x n` chessboard and returns the sequence of moves involved in the shortest path. The function should handle cases where the knight cannot move due to being surrounded by other pieces or if the destination is beyond the confines of the chessboard. Assume the chessboard is empty except for the knight. The function should be able to handle chessboards of any size `n`.
"""

from collections import deque 

def is_valid(i, j, visited, n):
    if i < 0 or j < 0 or i >= n or j >= n or visited[i][j]:
        return False
    return True

def possible_moves(x, y, visited, n):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    pos_moves = []
  
    for k in range(8):
        new_x, new_y = x+dx[k], y+dy[k]
  
        if is_valid(new_x, new_y, visited, n):
            pos_moves.append((new_x, new_y))
            
    return pos_moves

def knight_moves(src, dest, n):
    visited = [[False for _ in range(n)] for __ in range(n)]  
    visited[src[0]][src[1]] = True
  
    q = deque([(src, [])])  
    while len(q) > 0:
        cell, path = q.popleft()  
        i, j = cell

        if cell == dest:  
            return path + [cell]

        moves = possible_moves(i, j, visited, n)

        for move in moves:
            x, y = move 
            q.append((move, path + [cell]))  
            visited[x][y] = True  

    print("Path does not exist")  
    return False  