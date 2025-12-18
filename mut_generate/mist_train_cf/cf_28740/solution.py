"""
QUESTION:
Implement a function `countUniqueElements` that takes an array of integers and its size as input, and returns the count of unique elements in the array. A unique element is defined as an element that appears only once in the array. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def countUniqueElements(arr):
    """
    This function counts the number of unique elements in the given array.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: The count of unique elements in the array.
    """
    frequency_map = {}
    unique_count = 0

    # Count the frequency of each element in the array
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Count the number of unique elements
    for count in frequency_map.values():
        if count == 1:
            unique_count += 1

    return unique_count