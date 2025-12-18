"""
QUESTION:
Write a function `get_possible_moves_within_3_steps(x, y)` that takes the x and y coordinates of a knight on a circular 8x8 chessboard as input and returns a set of all possible moves the knight can make within 3 steps. The function should also print the total number of possible moves and each possible move within 3 steps. The knight's moves are the standard L-shaped moves, and the chessboard is circular, meaning the knight can "wrap around" from one side to the other.
"""

def is_valid_move(x, y):
    # Check if the move is within the circular chessboard
    return 0 <= x < 8 and 0 <= y < 8

def get_possible_moves(x, y):
    # List of possible moves for a knight
    moves = [(1, 2), (2, 1), (-1, 2), (-2, 1),
             (-1, -2), (-2, -1), (1, -2), (2, -1)]
    possible_moves = []
    for move in moves:
        new_x = (x + move[0]) % 8  # Wrap around if necessary
        new_y = (y + move[1]) % 8  # Wrap around if necessary
        if is_valid_move(new_x, new_y):
            possible_moves.append((new_x, new_y))
    return possible_moves

def get_possible_moves_within_3_steps(x, y):
    moves_within_3_steps = set()
    visited = set()

    def dfs(x, y, steps):
        # Base case: If we've reached 3 steps, return
        if steps == 3:
            return

        visited.add((x, y))
        possible_moves = get_possible_moves(x, y)
        for move in possible_moves:
            if move not in visited:
                moves_within_3_steps.add(move)
                dfs(move[0], move[1], steps + 1)
        visited.remove((x, y))

    dfs(x, y, 0)
    print("Total number of possible moves:", len(moves_within_3_steps))
    print("Possible moves within 3 steps:")
    for move in moves_within_3_steps:
        print(move)
    return moves_within_3_steps