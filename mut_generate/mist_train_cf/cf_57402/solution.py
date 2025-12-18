"""
QUESTION:
Reformulate a spiral-shaped grid of letters into a single word.

Write a function `spiral_word(grid)` that takes a 2D grid of characters as input and returns a string of alphabetical characters in the order they appear in a spiral pattern from top-left to bottom-right. The input grid can contain non-alphabetical characters and empty spaces, which should be excluded from the output.
"""

def spiral_word(grid):
    word = []
    while grid:
        word.extend(grid.pop(0))
        grid = list(zip(*grid))[::-1]
    return ''.join(char for group in word for char in group if char.isalpha())