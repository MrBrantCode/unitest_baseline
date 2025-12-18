"""
QUESTION:
Implement a function `index_to_notation(position: Tuple[int, int]) -> str` that converts a given chess board index position to its corresponding chess notation. The chess board is represented by an 8x8 grid with zero-based indices, where (0, 0) is the top-left corner and (7, 7) is the bottom-right corner. The chess notation should use a combination of a letter (indicating the column) and a number (indicating the row), where the letter is in lowercase and the number is between 1 and 8. The function should return the corresponding chess notation for the given position.
"""

from typing import Tuple

def index_to_notation(position: Tuple[int, int]) -> str:
    row, col = position
    return chr(97 + col) + str(8 - row)