"""
QUESTION:
Create a function called `sum_until_threshold` that iterates over the elements in a given list, keeping a running sum of the elements. The function should stop iterating when the running sum exceeds the product of the previous two elements. The function should return the running sum at the point where it exceeds the product of the previous two elements. The list will have at least three elements.
"""

def sum_until_threshold(lst):
    """
    This function calculates the running sum of elements in a list until it exceeds 
    the product of the previous two elements.

    Args:
        lst (list): A list of numbers with at least three elements.

    Returns:
        int: The running sum at the point where it exceeds the product of the previous two elements.
    """
    
    sum_so_far = 0
    threshold = 0
    
    for i in range(len(lst)):
        if i >= 2:
            threshold = lst[i-1] * lst[i-2]
        
        sum_so_far += lst[i]
        
        if i >= 2 and sum_so_far > threshold:
            break

    return sum_so_far