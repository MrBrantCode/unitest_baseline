"""
QUESTION:
Create a function named `sum_divisible_elements` that takes a 2D list as input. Assign 1 to all elements in the list that are divisible by 7 and return the sum of all the assigned elements. The 2D list will be a square array (i.e., have the same number of rows and columns).
"""

def sum_divisible_elements(arr):
    """
    This function takes a 2D list as input, assigns 1 to all elements in the list 
    that are divisible by 7, and returns the sum of all the assigned elements.
    
    Parameters:
    arr (list): A 2D list of integers
    
    Returns:
    int: The sum of all elements assigned 1 (i.e., divisible by 7)
    """
    total_sum = 0
    for row in arr:
        for element in row:
            if element % 7 == 0:
                total_sum += 1
    return total_sum