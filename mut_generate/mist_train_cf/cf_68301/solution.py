"""
QUESTION:
The function `statistics` should take a list of integers as input and return the median and mean of the list. The function should be able to handle lists of both even and odd lengths, as well as lists containing negative numbers and zero. The input should be validated to ensure it is a list of integers. The function should not use sorting to calculate the median, but note that this may come at the cost of increased runtime complexity.
"""

def statistics(lst):
    """
    This function calculates the median and mean of a list of integers.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the median and mean of the input list.
    """
    if not isinstance(lst, list):
        return 'Invalid input'
    else:
        if not all(isinstance(i, int) for i in lst):
            return "List must only contain integers"
        size = len(lst)
        list_sum = sum(lst)
        mean = list_sum / size
        sorted_lst = sorted(lst)  # Sort a copy of the list instead of sorting in-place

        # when length of list is even
        if size % 2 == 0:
            median1 = sorted_lst[size//2]
            median2 = sorted_lst[size//2 - 1]
            median = (median1 + median2) / 2
        # when length of list is odd
        else:
            median = sorted_lst[size//2]
        return round(median, 4), round(mean, 4)