"""
QUESTION:
Create a function named `convert_to_matrix` that takes a list of integers as input and returns a 5x5 matrix. If the input list has less than 25 elements, the resulting matrix should have fewer rows, but still 5 columns.
"""

def convert_to_matrix(nums):
    """
    Converts a list of integers into a 5x5 matrix.
    
    If the input list has less than 25 elements, the resulting matrix will have fewer rows, but still 5 columns.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A 5x5 matrix.
    """
    matrix = [nums[i:i + 5] for i in range(0, len(nums), 5)]
    return matrix