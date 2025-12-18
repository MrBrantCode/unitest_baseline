"""
QUESTION:
Write a function named `paper_folds` to calculate the number of times a piece of paper needs to be folded to reach a specified thickness. The function should take two parameters: `initial_thickness_mm`, the initial thickness of the paper in millimeters, and `target_thickness_meters`, the target thickness in meters. The function should return the minimum number of folds required to reach or exceed the target thickness.
"""

def paper_folds(initial_thickness_mm, target_thickness_meters):
    """
    Calculate the minimum number of folds required to reach or exceed a target thickness.
    
    Parameters:
    initial_thickness_mm (float): Initial thickness of the paper in millimeters.
    target_thickness_meters (float): Target thickness in meters.
    
    Returns:
    int: Minimum number of folds required.
    """
    thickness_paper = initial_thickness_mm / 1000  # Convert millimeters to meters
    num_folds = 0
    while thickness_paper < target_thickness_meters:
        thickness_paper *= 2
        num_folds += 1
    return num_folds