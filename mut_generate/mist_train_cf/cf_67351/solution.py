"""
QUESTION:
Create a function called `figureSkaterDirection` that takes a list of integers representing the degrees of rotation, where positive values represent a right spin and negative values represent a left spin. The function should return a string representing the final direction the figure skater is facing after all rotations, assuming they start facing north. The directions should be one of 'North', 'South', 'East', or 'West'.
"""

def figureSkaterDirection(rotation_degrees):
    """
    This function determines the final direction a figure skater is facing after a series of rotations.
    
    Parameters:
    rotation_degrees (list): A list of integers representing the degrees of rotation.
    
    Returns:
    str: The final direction the figure skater is facing, either 'North', 'South', 'East', or 'West'.
    """
    
    # Initialize the direction as 0 (north)
    initial_direction = 0
    
    # Perform each rotation successively
    for degree in rotation_degrees:
        initial_direction += degree
    
    # Get the equivalent degree within 360
    final_direction = initial_direction % 360
    
    # Determine the final direction based on the final degree
    if final_direction == 0 or final_direction == 360:
        return "North"
    elif final_direction == 90:
        return "East"
    elif final_direction == 180:
        return "South"
    elif final_direction == 270:
        return "West"
    # If the final degree is not a multiple of 90, the input is invalid
    else:
        return "Invalid input"