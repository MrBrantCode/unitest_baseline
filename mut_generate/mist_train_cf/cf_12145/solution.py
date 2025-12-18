"""
QUESTION:
Write a function `check_subset_and_count` that takes two lists of integers `subsetArray` and `supersetArray` as input. The function should return `True` if `subsetArray` is a subset of `supersetArray`, considering duplicate elements, and also return a dictionary containing the count of occurrences of each element in `subsetArray` within `supersetArray`. The function should handle arrays with negative integers and duplicate elements.
"""

def check_subset_and_count(subsetArray, supersetArray):
    """
    Checks if subsetArray is a subset of supersetArray, considering duplicate elements,
    and returns a dictionary containing the count of occurrences of each element in 
    subsetArray within supersetArray.

    Args:
        subsetArray (list): The potential subset list of integers.
        supersetArray (list): The potential superset list of integers.

    Returns:
        tuple: A boolean indicating whether subsetArray is a subset of supersetArray, 
               and a dictionary containing the count of occurrences of each element in 
               subsetArray within supersetArray.
    """
    subset_dict = {}
    
    # Count occurrences of each element in subsetArray
    for num in subsetArray:
        if num in subset_dict:
            subset_dict[num] += 1
        else:
            subset_dict[num] = 1
    
    # Check if subsetArray is a subset of supersetArray
    for num in subset_dict:
        if subset_dict[num] > supersetArray.count(num):
            return False, {}
    
    # Count occurrences of each element in subsetArray within supersetArray
    occurrences_dict = {}
    for num in subset_dict:
        occurrences_dict[num] = supersetArray.count(num)
    
    return True, occurrences_dict