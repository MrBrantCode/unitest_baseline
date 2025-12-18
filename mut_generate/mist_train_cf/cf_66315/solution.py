"""
QUESTION:
Write a function `remove_elements_from_vector` that removes elements from a given vector that are less than a certain threshold value. The function should iterate through the vector, and if an element is less than the threshold, it should be replaced with the last element of the vector and then removed. The function should return the modified vector. 

The function should take two parameters: a vector of integers and an integer representing the threshold value. 

Note: Be mindful of iterator invalidation when removing elements from the vector.
"""

def remove_elements_from_vector(vector, threshold):
    """
    Removes elements from a given vector that are less than a certain threshold value.
    
    Args:
        vector (list): A list of integers.
        threshold (int): An integer representing the threshold value.
    
    Returns:
        list: The modified vector.
    """
    
    for i in range(len(vector) - 1, -1, -1):
        if vector[i] < threshold:
            vector[i] = vector[-1]
            vector.pop()
    return vector