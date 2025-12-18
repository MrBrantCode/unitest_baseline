"""
QUESTION:
Write a function named `count_element_occurrences` that takes a list of elements as input and returns a dictionary where the keys are the elements in the list and the values are the number of occurrences of each element. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(k), where k is the number of unique elements in the list.
"""

def count_element_occurrences(input_list):
    """
    Counts the number of occurrences of each element in the input list.
    
    Args:
    input_list (list): The list of elements to count.
    
    Returns:
    dict: A dictionary where the keys are the elements in the list and the values are the number of occurrences of each element.
    """
    counts = {}
    for element in input_list:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts