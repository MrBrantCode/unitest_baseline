"""
QUESTION:
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other.
The positions will be passed as two arguments in algebraic notation.
For example, `knight("a3", "b5")` should return 1.

The knight is not allowed to move off the board.
The board is 8x8.

For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29

For information on algebraic notation, see
https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)
"""

from collections import deque

def knight_min_moves(start_pos, end_pos):
    moves = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
    
    # Convert the end position to coordinates
    target_x, target_y = ord(end_pos[0]) - 97, int(end_pos[1]) - 1
    
    # Initialize the queue with the starting position and move count
    queue = deque([(ord(start_pos[0]) - 97, int(start_pos[1]) - 1, 0)])
    seen = set()
    
    while queue:
        x, y, move_count = queue.popleft()
        
        # Check if we've reached the target position
        if x == target_x and y == target_y:
            return move_count
        
        # Skip if this position has already been visited
        if (x, y) in seen:
            continue
        
        # Mark this position as seen
        seen.add((x, y))
        
        # Explore all possible knight moves
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                queue.append((new_x, new_y, move_count + 1))
    
    # If no path is found (which shouldn't happen in a valid 8x8 board), return -1
    return -1