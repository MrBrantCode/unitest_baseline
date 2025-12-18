"""
QUESTION:
Write a function `categorize_elements` that takes an array as input and returns four lists: `numbers_divisible_by_3`, `numbers_not_divisible_by_3`, `non_numbers`, and `nested_lists`. The function should categorize each element in the input array based on whether it's an integer divisible by 3, an integer not divisible by 3, a non-integer (with "Not a number" appended), or a nested list.
"""

def categorize_elements(arr):
    """
    Categorize elements in an array into four lists: 
    numbers divisible by 3, numbers not divisible by 3, non-numbers, and nested lists.
    
    Parameters:
    arr (list): Input array containing various types of elements.
    
    Returns:
    tuple: A tuple of four lists: numbers_divisible_by_3, numbers_not_divisible_by_3, non_numbers, and nested_lists.
    """
    numbers_divisible_by_3 = []
    numbers_not_divisible_by_3 = []
    non_numbers = []
    nested_lists = []

    for element in arr:
        if isinstance(element, int) and element % 3 == 0:
            numbers_divisible_by_3.append(element)
        elif isinstance(element, int):
            numbers_not_divisible_by_3.append(element)
        elif isinstance(element, str):
            non_numbers.append(element + " Not a number")
        elif isinstance(element, list):
            nested_lists.append(element)

    return numbers_divisible_by_3, numbers_not_divisible_by_3, non_numbers, nested_lists