"""
QUESTION:
Write a function called `calculate_folds` that determines the number of times a piece of paper needs to be folded to reach a certain thickness. The function should take two parameters: `initial_thickness` in millimeters and `target_thickness` in miles. The function should return the minimum number of folds required to reach or exceed the target thickness.
"""

def calculate_folds(initial_thickness, target_thickness):
    """
    Calculate the minimum number of folds required to reach or exceed the target thickness.

    Parameters:
    initial_thickness (float): The initial thickness of the paper in millimeters.
    target_thickness (float): The target thickness in miles.

    Returns:
    int: The minimum number of folds required.
    """
    # Convert target thickness from miles to millimeters
    target_thickness_mm = target_thickness * 1609340
    
    # Initialize the number of folds and current thickness
    num_folds = 0
    current_thickness = initial_thickness

    # Continue folding until the target thickness is reached or exceeded
    while current_thickness < target_thickness_mm:
        current_thickness *= 2
        num_folds += 1

    return num_folds