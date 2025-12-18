"""
QUESTION:
Create a function `combine_lists` that takes two lists, `list_a` and `list_b`, as input. The function should return a new list that is the combination of `list_a` and `list_b`, where each element is a string in the format "letter: number". If `list_a` contains integers, they should be converted to their corresponding ASCII characters before combination. The resulting list should maintain the order of elements from the original lists and have a length equal to the sum of the lengths of `list_a` and `list_b`.
"""

def combine_lists(list_a, list_b):
    """
    Combine two lists into a new list where each element is a string in the format "letter: number".
    
    If list_a contains integers, they are converted to their corresponding ASCII characters before combination.
    
    The resulting list maintains the order of elements from the original lists and has a length equal to the sum of the lengths of list_a and list_b.
    
    Parameters:
    list_a (list): The first list, can contain strings or integers.
    list_b (list): The second list, contains integers.
    
    Returns:
    list: A new list with the combined elements.
    """
    new_list = []
    for i in range(len(list_a)):
        if isinstance(list_a[i], int):
            list_a[i] = chr(list_a[i])
        new_list.append(f"{list_a[i]}: {list_b[i]}")
    return new_list