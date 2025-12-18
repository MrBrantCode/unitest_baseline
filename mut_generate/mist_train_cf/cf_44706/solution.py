"""
QUESTION:
Create a function named `double_fifth_element` that takes a list as an argument and doubles the element at the fifth position (indexed at 4). The function should handle potential index errors if the list has fewer than five elements.
"""

def double_fifth_element(lst):
    """
    This function takes a list as an argument and doubles the element at the fifth position (indexed at 4).
    It handles potential index errors if the list has fewer than five elements.
    
    Parameters:
    lst (list): The input list
    
    Returns:
    list: The modified list with the fifth element doubled if it exists
    """
    try:
        lst[4] = lst[4] * 2
    except IndexError:
        print("The array has fewer than five elements.")
    return lst