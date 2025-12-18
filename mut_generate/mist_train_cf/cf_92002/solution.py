"""
QUESTION:
Write a function named `sort_tuples` that takes a list of tuples as input. Each tuple contains two integers. The function should sort the list based on the sum of the integers in each tuple, in descending order, and exclude any tuples where the sum of the integers is less than or equal to 5. The function should return the sorted list only if it contains at least 3 tuples; otherwise, it should return None.
"""

def sort_tuples(tuples_list):
    """
    Sorts a list of tuples based on the sum of the integers in each tuple, in descending order, 
    and excludes any tuples where the sum of the integers is less than or equal to 5.
    
    Args:
        tuples_list (list): A list of tuples containing two integers each.
    
    Returns:
        list: The sorted list of tuples if it contains at least 3 tuples; otherwise, None.
    """
    # Sort the list of tuples based on the sum of the integers in each tuple in descending order
    sorted_list = sorted(tuples_list, key=lambda x: sum(x), reverse=True)
    
    # Filter out tuples with a sum less than or equal to 5
    filtered_list = list(filter(lambda x: sum(x) > 5, sorted_list))
    
    # Return the sorted list if it contains at least 3 tuples; otherwise, return None
    return filtered_list if len(filtered_list) >= 3 else None