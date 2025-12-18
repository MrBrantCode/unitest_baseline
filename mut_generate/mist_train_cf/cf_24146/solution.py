"""
QUESTION:
Create a function `permute` that takes a list of elements as input and returns all possible permutations of the elements in the list. The function should handle lists of any length.
"""

def permute(elements):
    """
    Returns all possible permutations of the elements in the list.
    
    Args:
    elements (list): A list of elements.
    
    Returns:
    list: A list of lists, where each sublist is a permutation of the input elements.
    """
    if len(elements) == 0:
        return [] 
    if len(elements) == 1:
        return [elements] 
  
    result = [] 
    for i in range(len(elements)):
        current = elements[i] 
  
        remaining_elements = elements[:i] + elements[i+1:] 
  
        for p in permute(remaining_elements): 
            result.append([current] + p) 
    return result