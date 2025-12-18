"""
QUESTION:
Create a function `create_game_board(n)` that generates an n x n 2D list filled with zeros, representing a Nim game board of size n x n.
"""

def create_game_board(n):
    return [[0]*n for _ in range(n)]