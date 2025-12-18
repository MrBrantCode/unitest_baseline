"""
QUESTION:
Write a function `find_common_items(arr1, arr2)` that takes two inputs, `arr1` and `arr2`, which can be either lists or strings of comma-separated numbers. The function should return a list of common numbers between `arr1` and `arr2` without modifying the original inputs. The function should handle the case where either `arr1` or `arr2` is a string instead of a list and should not use any built-in functions or libraries to find the common items.
"""

def find_common_items(arr1, arr2):
    """
    This function finds the common numbers between two inputs, 
    which can be either lists or strings of comma-separated numbers.

    Args:
        arr1 (list or str): The first list or string of numbers.
        arr2 (list or str): The second list or string of numbers.

    Returns:
        list: A list of common numbers between arr1 and arr2.
    """

    # Convert arr1 and arr2 to lists if they are strings
    if isinstance(arr1, str):
        arr1 = arr1.split(', ')
        arr1 = [int(num) for num in arr1]
        
    if isinstance(arr2, str):
        arr2 = arr2.split(', ')
        arr2 = [int(num) for num in arr2]

    # Find the common items
    common_items = []
    for item in arr1:
        if item in arr2:
            common_items.append(item)
    return common_items