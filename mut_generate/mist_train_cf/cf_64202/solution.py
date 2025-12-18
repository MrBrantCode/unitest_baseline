"""
QUESTION:
Create a bijective mapping for a given 3-dimensional matrix composed of decimal numbers. The function should take a 3D list of decimal numbers as input and return a dictionary where the keys are tuples representing the indices in the 3D matrix and the values are the corresponding decimal numbers. The function should ensure that the mapping is bijective, meaning every indices tuple in the 3D matrix is unique and each indices tuple maps to a unique decimal number. 

The input 3D list should be in the format [[[decimal, decimal, ...], [decimal, decimal, ...], ...], [[decimal, decimal, ...], [decimal, decimal, ...], ...], ...] where each decimal is a unique number. The function should work for any size of 3D matrix. 

The function name should be bijectiveMapping.
"""

def bijective_mapping(lst):
    """
    Creates a bijective mapping for a given 3-dimensional matrix composed of decimal numbers.
    
    Args:
        lst (list): A 3D list of decimal numbers.
    
    Returns:
        dict: A dictionary where the keys are tuples representing the indices in the 3D matrix and the values are the corresponding decimal numbers.
    """
    mapping = {}
    for i, l1 in enumerate(lst):
        for j, l2 in enumerate(l1):
            for k, val in enumerate(l2):
                mapping[(i, j, k)] = val
    return mapping