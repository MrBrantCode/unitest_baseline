"""
QUESTION:
Calculate the harmonic mean of a series of numbers using a function named `harmonic_mean`. The input will be an array of positive integers. The harmonic mean is defined as the number of elements divided by the sum of the reciprocals of the elements. The function should return the calculated harmonic mean.
"""

def harmonic_mean(arr):
    """
    Calculate the harmonic mean of a series of numbers.
    
    The harmonic mean is defined as the number of elements divided by 
    the sum of the reciprocals of the elements.
    
    Parameters:
    arr (list): A list of positive integers.
    
    Returns:
    float: The calculated harmonic mean.
    """
    return len(arr) / sum(1/x for x in arr)