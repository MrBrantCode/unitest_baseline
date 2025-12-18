"""
QUESTION:
You have two boxes of apples with different weights. One box contains apples weighing 200g each and the other contains apples weighing 500g each. Given that there are a total of 12 apples and their combined weight is 4.4kg (4400g), write a function `calculate_apple_counts` that calculates and returns the number of small apples and the number of big apples. The function should handle cases where it's impossible to find an exact integer solution due to incorrect or inconsistent input conditions.
"""

def calculate_apple_counts(total_apples, total_weight):
    """
    Calculate the number of small apples (200g each) and the number of big apples (500g each) 
    given the total number of apples and their combined weight.

    Args:
        total_apples (int): The total number of apples.
        total_weight (int): The total weight of the apples in grams.

    Returns:
        tuple: A tuple containing the number of small apples and the number of big apples. 
               If it's impossible to find an exact integer solution, returns None.
    """
    # Calculate the number of small apples
    s = (total_weight - 500 * total_apples) / (200 - 500)
    
    # Check if the number of small apples is an integer
    if s.is_integer() and s >= 0 and s <= total_apples:
        # Calculate the number of big apples
        b = total_apples - int(s)
        return (int(s), b)
    else:
        # If it's impossible to find an exact integer solution, return None
        return None