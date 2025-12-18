"""
QUESTION:
Write a function `count_elements` that takes two parameters: an element and a potentially nested list. The function should return the number of times the specified element occurs within the list. The function should be able to handle nested lists, tuples, and sets, and should ignore any duplicates within sets.
"""

def count_elements(element, data):
    """
    This function counts the occurrences of a specified element in a potentially nested list.
    
    It can handle nested lists, tuples, and sets, and ignores any duplicates within sets.
    
    Parameters:
    element (any): The element to be searched in the list.
    data (list): A potentially nested list containing the element.
    
    Returns:
    int: The number of occurrences of the element in the list.
    """
    count = 0
    for i in data:
        if type(i) in [list, tuple, set]:
            count += count_elements(element, i)
        else:
            if i == element:
                count += 1
    return count