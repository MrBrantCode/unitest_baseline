"""
QUESTION:
Create a function named `singleton_positions` that takes an array of integers as input. The function should return a list of indices of the singleton elements in the array, where a singleton element is an element that appears only once in the array. The input array may contain negative and positive integers, zeroes, and may have more than one singleton element. The function should use only basic programming constructs and not any external libraries or functions.
"""

def singleton_positions(arr):
    """
    Returns a list of indices of the singleton elements in the array.
    
    A singleton element is an element that appears only once in the array.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    list: A list of indices of the singleton elements.
    """
    element_counts = {}
    singletons = []
    positions = []
    
    # Count the occurrences of each number in the list
    for num in arr:
        if num in element_counts:
            element_counts[num] += 1
        else:
            element_counts[num] = 1
    
    # Identify the singleton numbers
    for num, count in element_counts.items():
        if count == 1:
            singletons.append(num)
    
    # Get the indices of each singleton number
    for i in range(len(arr)):
        if arr[i] in singletons:
            positions.append(i)
    
    return positions