"""
QUESTION:
Write a function `sort_tuple` that takes a tuple of integers as input, rearranges the elements in descending order, and places the largest even number at the beginning and the largest odd number at the end.
"""

def sort_tuple(input_tuple):
    """
    This function rearranges the elements in a tuple of integers in descending order, 
    places the largest even number at the beginning, and the largest odd number at the end.

    Args:
    input_tuple (tuple): A tuple of integers.

    Returns:
    tuple: The rearranged tuple.
    """
    # Convert the tuple into list
    input_list = list(input_tuple)
    
    # Split into even and odd numbers
    even_num = [x for x in input_list if x % 2 == 0]
    odd_num = [x for x in input_list if x % 2 != 0]

    # Sort each list in descending order
    even_num.sort(reverse=True)
    odd_num.sort(reverse=True)

    # Join the list with the largest even number at the beginning and the largest odd number at the end
    if even_num and odd_num:
        sorted_list = even_num + odd_num[1:] + [odd_num[0]]
    elif even_num:
        sorted_list = even_num
    else:
        sorted_list = odd_num

    # Convert it back into tuple
    sorted_tuple = tuple(sorted_list)
    
    return sorted_tuple