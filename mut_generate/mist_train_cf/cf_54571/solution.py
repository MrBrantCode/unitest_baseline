"""
QUESTION:
Create a function `find_negatives` that takes a list of integers as input. The function should return the first negative integer, its index position in the original list, the total count of negative integers, and a new list containing all the negative integers in their original order of appearance. If there are no negative integers in the list, the function should return None for the first negative integer and its index position.
"""

def find_negatives(numbers):
    """
    Returns the first negative integer, its index position in the original list, 
    the total count of negative integers, and a new list containing all the 
    negative integers in their original order of appearance.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the first negative integer, its index position, 
        the total count of negative integers, and a list of all negative integers.
    """
    negatives = [num for num in numbers if num < 0]
    first_negative = negatives[0] if negatives else None
    first_negative_index = numbers.index(first_negative) if negatives else None
    count_negatives = len(negatives)
    return first_negative, first_negative_index, count_negatives, negatives