"""
QUESTION:
Implement the `get_positive_and_sort_dict` function. The function takes a dictionary `d` where each key is associated with a list of integers. It should return a new dictionary with the same keys, but the values should only include positive numbers and be sorted in ascending order. Zero should not be considered a positive number.
"""

def get_positive_and_sort_dict(d: dict):
    """
    Return only positive numbers in the dictionary values, sorted in ascending order.
    """
    
    def get_positive_and_sort_list(lst):
        # Use list comprehension to create a new list containing only positive numbers.
        positive_nums = [num for num in lst if num > 0]
        
        # Sort list in ascending order.
        positive_nums.sort()
        
        return positive_nums

    result_dict = {}
    for k, v in d.items():
        result_dict[k] = get_positive_and_sort_list(v)
        
    return result_dict