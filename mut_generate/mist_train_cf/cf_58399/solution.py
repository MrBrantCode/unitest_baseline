"""
QUESTION:
Create a function called `compare_diameters` that takes a list of floating point numbers representing human hair diameters in millimeters. The function should return an inequality that correctly compares the diameters of all hair strands in ascending order, without using any statistical measures such as averages. The input list may contain any number of diameters.
"""

def compare_diameters(diameters):
    """
    This function takes a list of floating point numbers representing human hair diameters in millimeters.
    It returns an inequality that correctly compares the diameters of all hair strands in ascending order.
    
    Parameters:
    diameters (list): A list of floating point numbers representing human hair diameters in millimeters.
    
    Returns:
    str: An inequality that compares the diameters of all hair strands in ascending order.
    """
    # Sort the diameters in ascending order
    diameters.sort()
    
    # Create the inequality string
    inequality = ''
    for i in range(len(diameters)-1):
        inequality += f'{diameters[i]} <= {diameters[i+1]} '
    
    return inequality