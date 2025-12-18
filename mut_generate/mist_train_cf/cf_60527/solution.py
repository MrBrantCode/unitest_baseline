"""
QUESTION:
Create a function named `set_symmetric_difference` that takes two linked lists `s1` and `s2`, and an optional parameter `exclude` of type integer. The function should return a list of elements that are present in either `s1` or `s2` but not in both, excluding the `exclude` value if provided. The returned list should be sorted and contain no duplicates. Implement the function with a time complexity less than O(n^2).
"""

from typing import Optional

def set_symmetric_difference(s1: list, s2: list, exclude: Optional[int] = None):
    """
    This function takes two lists and an optional exclude parameter.
    It returns a list of elements that are present in either list but not in both, 
    excluding the exclude value if provided. The returned list is sorted and contains no duplicates.

    Args:
        s1 (list): The first list.
        s2 (list): The second list.
        exclude (Optional[int], optional): The value to exclude. Defaults to None.

    Returns:
        list: A list of elements that are present in either list but not in both.
    """

    # Create a set to store unique elements from both lists
    d = set(s1 + s2)
    
    # If exclude is not None, remove it from the set
    if exclude is not None:
        d.discard(exclude)
    
    # Find the symmetric difference
    symmetric_diff = list(set(s1) ^ set(s2))
    
    # Remove the excluded value if it's in the symmetric difference
    if exclude is not None and exclude in symmetric_diff:
        symmetric_diff.remove(exclude)
    
    # Sort the symmetric difference
    symmetric_diff.sort()
    
    return symmetric_diff