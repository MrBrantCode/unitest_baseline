"""
QUESTION:
Write a function `compute_unique_aggregate` that calculates the sum of all unique elements in a 4D array. The input array is a list of lists of lists of lists of integers. The function should return the aggregate value of unique integers in the array.
"""

def compute_unique_aggregate(arr):
    """
    Calculate the sum of all unique elements in a 4D array.
    
    Parameters:
    arr (list): A list of lists of lists of lists of integers.
    
    Returns:
    int: The aggregate value of unique integers in the array.
    """
    # Flatten the array and remove duplicates using set()
    flat_arr = set(num for sublist1 in arr for sublist2 in sublist1 for sublist3 in sublist2 for num in sublist3)
    
    # Compute the aggregate value
    return sum(flat_arr)