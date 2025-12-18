"""
QUESTION:
Write a function `count_right_triangles(n)` that calculates the number of right triangles that can be formed with a right angle at point `C(0,50)`, given that the coordinates of points `A` and `B` lie between `0` and `n` inclusive. The function should return the total number of right triangles.
"""

def count_right_triangles(n):
    """
    Calculate the number of right triangles that can be formed with a right angle at point C(0,50),
    given that the coordinates of points A and B lie between 0 and n inclusive.
    
    Args:
        n (int): The upper limit of the coordinates of points A and B.
    
    Returns:
        int: The total number of right triangles.
    """
    totalTriangles = 3 * n * (n+1) * (n+2) // 2  # for 1st and 2nd case
    totalTriangles += 2 * n * n  # for 3rd case
    return totalTriangles