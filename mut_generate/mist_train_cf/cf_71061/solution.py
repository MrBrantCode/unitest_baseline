"""
QUESTION:
Write a function `calculate_boxes` that calculates the minimum number of boxes required to pack a certain number of shirts. Each box can hold a fixed number of shirts, and the boxes must be filled to maximum capacity without exceeding the total order quantity. The function should take two parameters: `total_shirts` and `shirts_per_box`.
"""

def calculate_boxes(total_shirts, shirts_per_box):
    """
    Calculate the minimum number of boxes required to pack a certain number of shirts.

    Parameters:
    total_shirts (int): The total number of shirts to be packed.
    shirts_per_box (int): The number of shirts each box can hold.

    Returns:
    int: The minimum number of boxes required.
    """
    total_boxes = total_shirts // shirts_per_box
    return total_boxes