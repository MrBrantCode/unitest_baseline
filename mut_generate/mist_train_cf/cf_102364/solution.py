"""
QUESTION:
Write a function called "reverse_list" that takes a list of integers as input, and returns a new list with the elements in reverse order without modifying the original list. The time complexity should be O(n), where n is the length of the input list. Additionally, write code to print the first and last value of the input list. The input list will not exceed 10^6 elements and will only contain integers between 1 and 1000. The implementation should not use any built-in functions or libraries for reversing the list.
"""

def reverse_list(input_list):
    """
    Reverses a list of integers without modifying the original list.

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list with the elements in reverse order.
    """
    reversed_list = []
    for i in range(len(input_list)-1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list