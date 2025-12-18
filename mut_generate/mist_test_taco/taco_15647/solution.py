"""
QUESTION:
# Grains

Write a program that calculates the number of grains of wheat on a chessboard given that the number on each square is double the previous one.

There are 64 squares on a chessboard.

#Example:
square(1) = 1
square(2) = 2
square(3) = 4
square(4) = 8
etc...

Write a program that shows how many grains were on each square
"""

def calculate_grains_on_square(square_number: int) -> int:
    """
    Calculate the number of grains of wheat on a specific square of a chessboard,
    where the number on each square is double the previous one.

    :param square_number: The number of the square on the chessboard (1 to 64).
    :return: The number of grains on the specified square.
    """
    return 2 ** (square_number - 1)