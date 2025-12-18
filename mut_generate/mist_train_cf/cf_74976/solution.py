"""
QUESTION:
Write a function `bfs` that calculates the minimum number of moves a knight piece can make to transition from a specified starting position to a specified ending position within the confines of a standard 8x8 chessboard, where the knight's movements are restricted to the standard chess piece movements. The function should take two parameters, `start` and `end`, representing the starting and ending positions as tuples (x, y) with the origin (0, 0) at the top left square of the board. The function should return the minimum number of moves if a valid path exists, or None otherwise.
"""

from collections import deque

def is_valid(pos):
    """This function checks if a position is within the chess board"""
    x, y = pos
    if x < 0 or y < 0 or x >= 8 or y >= 8:
        return False
    return True 

def bfs(start, end):
    """This function uses BFS to find the minimum moves a knight can make from the starting position to the ending position"""
    directions = [(2,1),(1,2),(2,-1),(1,-2),(-2,1),(-1,2),(-2,-1),(-1,-2)]  # all possible moves of the knight
    queue = deque([(start, 0)])  # use deque to implement a queue
    visited = set()  # a set to record visited positions 
    while queue:  
        current_pos, current_moves = queue.popleft()  # deque from the left of the queue
        if current_pos == end:
            return current_moves  # if the current position is the ending position, return the current moves
        for direction in directions:
            next_x, next_y = current_pos[0] + direction[0], current_pos[1] + direction[1]  # calculate next possible positions
            next_pos = (next_x, next_y)
            if is_valid(next_pos) and next_pos not in visited:  # if the next position is valid and not visited
                queue.append((next_pos, current_moves + 1))  # append it to the right of the queue, with current moves plus 1
                visited.add(next_pos)  # add it to the visited set
    return None 