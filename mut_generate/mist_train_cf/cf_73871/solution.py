"""
QUESTION:
Write a function named `check_vc_dimension` that determines if the given number of points can be shattered by a line in 1-dimensional space. The function should return True if the VC dimension of a line is greater than or equal to the given number of points and False otherwise. Assume that the number of points will be a positive integer.
"""

def check_vc_dimension(num_points):
    """
    This function determines if the given number of points can be shattered by a line in 1-dimensional space.
    
    Parameters:
    num_points (int): The number of points to check.
    
    Returns:
    bool: True if the VC dimension of a line is greater than or equal to the given number of points, False otherwise.
    """
    # The VC dimension of a line in 1-dimensional space is 2
    vc_dimension = 2
    
    # Check if the VC dimension is greater than or equal to the given number of points
    return num_points <= vc_dimension