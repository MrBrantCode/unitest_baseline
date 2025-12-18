"""
QUESTION:
Write a function `total_apple_pies` that takes three parameters: the number of boxes of apples, the number of apples in each box, and the number of apples required per apple pie. The function should return the total number of apple pies that can be baked given the present supply of apples, assuming the bakers cannot bake a fraction of a pie.
"""

def total_apple_pies(boxes, apples_per_box, apples_per_pie):
    """
    Calculate the total number of apple pies that can be baked given the present supply of apples.

    Parameters:
    boxes (int): The number of boxes of apples.
    apples_per_box (int): The number of apples in each box.
    apples_per_pie (int): The number of apples required per apple pie.

    Returns:
    int: The total number of apple pies that can be baked.
    """
    total_apples = boxes * apples_per_box
    return total_apples // apples_per_pie