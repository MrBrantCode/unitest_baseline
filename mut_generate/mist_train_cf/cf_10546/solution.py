"""
QUESTION:
Write a function `combine_lists` that takes two lists `list_a` and `list_b` as input, where `list_a` contains strings and `list_b` contains integers. The function should return a new list that combines the elements from `list_a` and `list_b` in the format "letter: number" while maintaining their original order. The length of the resulting list should be equal to the sum of the lengths of the original lists.
"""

def combine_lists(list_a, list_b):
    """
    Combine elements from two lists into a new list in the format "letter: number".

    Args:
        list_a (list): A list of strings.
        list_b (list): A list of integers.

    Returns:
        list: A new list combining elements from list_a and list_b.
    """
    result = []
    min_len = min(len(list_a), len(list_b))
    
    # Combine elements up to the length of the shorter list
    result = [f"{a}: {b}" for a, b in zip(list_a[:min_len], list_b[:min_len])]
    
    # Append any remaining elements from the longer list
    if len(list_a) > len(list_b):
        result += [f"{a}: None" for a in list_a[min_len:]]
    elif len(list_b) > len(list_a):
        result += [f"None: {b}" for b in list_b[min_len:]]
    
    return result