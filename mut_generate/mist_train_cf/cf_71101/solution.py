"""
QUESTION:
Implement a function `bubble_sort(arr)` that sorts an array in ascending order using an optimized bubble sort algorithm, which stops early if the list is already sorted. The function should be able to handle both lists of integers and lists of dictionaries, with the latter being sorted based on a specified key.

The function `bubble_sort_dict(dict_list, sort_key)` should be able to sort a list of dictionaries based on the values of a specified key. 

Note: The input can be either a list of integers or a list of dictionaries, and the function should handle both cases accordingly.
"""

def entrance(arr, sort_key=None):
    """
    Sorts an array in ascending order using an optimized bubble sort algorithm.
    
    If the input is a list of dictionaries, the function will sort based on a specified key.
    
    Args:
        arr (list): A list of integers or dictionaries to be sorted.
        sort_key (str, optional): Key to sort by if the input is a list of dictionaries. Defaults to None.
    
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sort_key is not None:
                # If the input is a list of dictionaries
                if arr[j][sort_key] > arr[j + 1][sort_key]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            else:
                # If the input is a list of integers
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        # if no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr