"""
QUESTION:
Write a function `find_common_items(arr1, arr2)` that takes two inputs, `arr1` and `arr2`, which can be either lists of integers or a string of comma-separated integers. The function should return a list of common integers between `arr1` and `arr2` without modifying the original inputs. If `arr2` is a string, it should be converted to a list of integers before finding the common items. The function should only use basic programming constructs such as loops and conditionals, and should not use any built-in functions or libraries to find the common items.
"""

def find_common_items(arr1, arr2):
    """
    This function finds the common integers between two inputs, arr1 and arr2.
    
    Parameters:
    arr1 (list): A list of integers.
    arr2 (list or str): A list of integers or a string of comma-separated integers.
    
    Returns:
    list: A list of common integers between arr1 and arr2.
    """
    
    # Convert arr2 to a list if it is a string
    if isinstance(arr2, str):
        arr2 = arr2.split(', ')
        arr2 = [int(num) for num in arr2]
    
    # Find the common items
    common_items = []
    for item in arr1:
        if item in arr2:
            common_items.append(item)
    
    return common_items