"""
QUESTION:
Compute the quantity of apples in a fruit stall given the total number of fruits and their distribution ratio. 

Function name: compute_apples 
Input: total_fruits (integer) and ratio (list or string of two numbers) 
Output: The number of apples as an integer 
Restriction: total_fruits is a positive integer, and ratio is a list or string representing the distribution of apples and pineapples, e.g., '2:3' or [2, 3].
"""

def compute_apples(total_fruits, ratio):
    """
    Compute the quantity of apples in a fruit stall given the total number of fruits and their distribution ratio.

    Args:
        total_fruits (int): The total number of fruits.
        ratio (list or str): A list or string representing the distribution of apples and pineapples.

    Returns:
        int: The number of apples.
    """
    if isinstance(ratio, str):
        ratio = list(map(int, ratio.split(':')))
    
    total_parts = sum(ratio)
    part_value = total_fruits // total_parts
    return ratio[0] * part_value