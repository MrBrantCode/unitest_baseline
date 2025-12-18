"""
QUESTION:
Create a function `custom_sort` that takes a list containing mixed variable types (integers, strings, and lists) as input. The function should return a new list where the integers remain in their original positions, strings are sorted alphabetically, and lists are sorted based on the concatenated string representation of their string elements (ignoring integers).
"""

def custom_sort(lst):
    """
    Sorts a list containing mixed variable types (integers, strings, and lists).
    The function returns a new list where the integers remain in their original positions, 
    strings are sorted alphabetically, and lists are sorted based on the concatenated string 
    representation of their string elements (ignoring integers).
    
    Parameters:
    lst (list): A list containing mixed variable types.
    
    Returns:
    list: A new list with sorted strings and lists, and integers in their original positions.
    """
    strs = []
    lists = []
    ints = []
  
    # separate strings, lists, and integers from the input list
    for i in lst:
        if isinstance(i, int):
            ints.append(i)
        elif isinstance(i, str):
            strs.append(i)
        elif isinstance(i, list):
            list_str = "".join([str(x) for x in i if isinstance(x, str)])
            lists.append((list_str, i))
            
    # sort strings
    sorted_strs = sorted(strs)

    # sort lists
    sorted_lists = sorted(lists, key=lambda x: x[0])
    sorted_lists = [x[1] for x in sorted_lists]

    # combine integers, sorted strings, and sorted lists
    result = []
    int_index = 0
    for i in lst:
        if isinstance(i, int):
            result.append(ints[int_index])
            int_index += 1
        elif isinstance(i, str):
            result.append(sorted_strs.pop(0))
        elif isinstance(i, list):
            result.append(sorted_lists.pop(0))

    return result