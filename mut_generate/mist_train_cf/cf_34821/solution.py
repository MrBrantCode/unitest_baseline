"""
QUESTION:
Implement a function `move_player_and_box` that simulates the movement of a player and a box in a grid-based game environment. The function takes as input the grid, the current positions of the player and the box, the target position, a list of impassable positions, and a move direction ('U', 'D', 'L', or 'R'). It returns the new positions of the player and the box after executing the move, following these rules:

- The player and the box can only move to an adjacent cell if it is not impassable.
- If the player pushes the box into the target position, the game is won, and the box cannot be moved further.

The grid is a 2D list of characters, where each character represents the content of the corresponding cell: 'P' for the player, '2' for the box, 'T' for the target, '#' for impassable positions, and '.' for empty cells.
"""

def move_player_and_box(grid, player_position, box_position, target_position, impassable_positions, move):
    def is_valid_position(position):
        row, col = position
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] not in ['#', '2']

    def move_position(position, direction):
        row, col = position
        if direction == 'U':
            return row - 1, col
        elif direction == 'D':
            return row + 1, col
        elif direction == 'L':
            return row, col - 1
        elif direction == 'R':
            return row, col + 1

    def is_win_state(box_position, target_position):
        return box_position == target_position

    new_player_position = move_position(player_position, move)
    new_box_position = box_position

    if new_player_position == box_position:
        new_box_position = move_position(box_position, move)

    if is_valid_position(new_player_position) and is_valid_position(new_box_position):
        if is_win_state(new_box_position, target_position):
            return new_player_position, new_box_position
        elif grid[new_box_position[0]][new_box_position[1]] != '#':
            return new_player_position, new_box_position

    return player_position, box_position