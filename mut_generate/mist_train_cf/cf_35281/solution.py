"""
QUESTION:
Write a function `parse_game_board(grid)` that takes a 2D list of characters `grid` as input and returns a dictionary containing the count of each unique character in the grid. The grid may contain color code escape sequences represented as '\033[Xm', where X is a number representing a color. The function should iterate through each character in the grid and update the count in the dictionary. The dictionary should have keys for each unique character and the color codes, and the values should be the count of occurrences of each character or color code in the grid.
"""

def parse_game_board(grid):
    counts = {}
    for row in grid:
        for char in row:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts