"""
QUESTION:
Create a function `cumul_sum` that takes a tuple as input, recursively calculates the cumulative sum of all numerical values (including complex numbers' real parts) within the tuple and its nested structures, and ignores non-numeric entities. The function should handle integers, floats, and complex numbers.
"""

def cumul_sum(tuples):
    """
    Recursively calculates the cumulative sum of all numerical values 
    (including complex numbers' real parts) within the tuple and its nested structures, 
    and ignores non-numeric entities.

    Args:
        tuples (tuple): Input tuple that can contain integers, floats, complex numbers, 
                        and nested tuples.

    Returns:
        float: The cumulative sum of all numerical values in the input tuple.
    """
    total = 0
    for i in tuples:
        if isinstance(i, tuple):
            total += cumul_sum(i)
        elif isinstance(i, (int, float)):
            total += i
        elif isinstance(i, complex):
            total += i.real
    return total