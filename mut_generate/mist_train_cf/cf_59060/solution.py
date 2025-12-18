"""
QUESTION:
Write a function named `calculate_availability` that takes two parameters: `mtbf` (Mean Time Between Failures) and `mttr` (Mean Time To Repair). This function should calculate and return the system availability using the formula `availability = mtbf / (mtbf + mttr)`.
"""

def calculate_availability(mtbf, mttr):
    """
    Calculate the system availability using the formula:
    availability = mtbf / (mtbf + mttr)
    
    Parameters:
    mtbf (float): Mean Time Between Failures
    mttr (float): Mean Time To Repair
    
    Returns:
    float: System availability
    """
    return mtbf / (mtbf + mttr)