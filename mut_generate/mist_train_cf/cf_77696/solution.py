"""
QUESTION:
Write a function named bulletin_board_area that calculates the total area of a bulletin board that can be entirely covered by square pieces of paper without any empty spots or overlaps. The function should take the dimensions of a single square piece of paper (length and width in feet) and the total number of pieces as input, and return the total area of the bulletin board in square feet. Assume the length and width of the square pieces are 1 foot each and the total number of pieces is 30.
"""

def bulletin_board_area(length, width, total_pieces):
    """
    Calculate the total area of a bulletin board that can be entirely covered by square pieces of paper.

    Args:
        length (float): The length of a single square piece of paper in feet.
        width (float): The width of a single square piece of paper in feet.
        total_pieces (int): The total number of square pieces required to cover the board.

    Returns:
        float: The total area of the bulletin board in square feet.
    """
    # calculate the area of one square piece
    area_piece = length * width

    # calculate the total area of the bulletin board
    total_area = total_pieces * area_piece
    return total_area