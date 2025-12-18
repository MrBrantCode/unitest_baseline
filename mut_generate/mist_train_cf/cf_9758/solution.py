"""
QUESTION:
Create a function `findThreeDuplicates(A)` that takes an array `A` as input. Return the indices of elements that appear exactly three times in the array. The function should return an empty list if no element appears exactly three times or if more than one element appears exactly three times.
"""

def findThreeDuplicates(A):
    """
    Return the indices of elements that appear exactly three times in the array.
    If no element appears exactly three times or if more than one element appears 
    exactly three times, return an empty list.
    
    Args:
        A (list): The input array.
    
    Returns:
        list: The indices of elements that appear exactly three times.
    """
    occurrences = {}
    for num in A:
        if num not in occurrences:
            occurrences[num] = [1]
        else:
            occurrences[num].append(1)
    
    duplicateIndices = []
    for key, value in occurrences.items():
        if len(value) == 3:
            duplicateIndices.extend([i for i, x in enumerate(A) if x == key])
        if len(duplicateIndices) > 3:
            return []
    
    if len(duplicateIndices) != 3:
        return []
    
    return duplicateIndices