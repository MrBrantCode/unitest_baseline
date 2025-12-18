"""
QUESTION:
Write a function named `sort_cubed_aggregate` that takes a list of elements as input, computes the cube of each numeric element, sums them up, and sorts the resulting cubical values in descending order. The function should ignore non-numeric elements and handle edge cases where the input list is empty.
"""

def sort_cubed_aggregate(numbers):
    """
    Compute the cube of each numeric element in the input list, 
    sum them up, and sort the resulting cubical values in descending order.
    
    Args:
        numbers (list): A list of elements.
    
    Returns:
        list: A list of cubed numbers in descending order.
    """
    cubed_sum = []
    for n in numbers:
        try:
            cubed_sum.append(n**3)
        except TypeError:
            continue
    cubed_sum.sort(reverse=True)
    return cubed_sum