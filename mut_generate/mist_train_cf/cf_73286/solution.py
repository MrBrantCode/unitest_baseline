"""
QUESTION:
Develop a function called `remove_values` that takes two parameters: `arr1` and `arr2`. `arr1` is a list of integers and `arr2` is a dictionary with a key 'values' containing a list of integers to be removed from `arr1`. The function should return a new list with all occurrences of the values from `arr2` removed from `arr1`. The function should also handle edge cases where `arr1` or `arr2` are empty or `arr2` does not contain the key 'values'.
"""

def remove_values(arr1, arr2):
    if not arr1 or not arr2:
        return []
    if isinstance(arr2, dict) and 'values' in arr2:
        arr2 = arr2.get('values')
    else:
        return []
    
    # Convert arr2 list to set for faster lookup
    arr2_set = set(arr2)
    
    # Create new list without specific values
    arr1 = [i for i in arr1 if i not in arr2_set]

    return arr1