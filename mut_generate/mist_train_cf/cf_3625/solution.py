"""
QUESTION:
Write a function named `sort_even_numbers` that takes a list of integers as input, removes any duplicate even numbers, sorts the remaining even numbers in ascending order without using built-in sorting functions or libraries, and returns the sorted list of even numbers. The function should handle both positive and negative integers.
"""

def sort_even_numbers(lst):
    """
    This function takes a list of integers, removes any duplicate even numbers, 
    sorts the remaining even numbers in ascending order, and returns the sorted list.

    Args:
    lst (list): A list of integers.

    Returns:
    list: A sorted list of even numbers.
    """
    even_numbers = []
    for num in lst:
        if num % 2 == 0 and num not in even_numbers:
            even_numbers.append(num)
    for i in range(len(even_numbers)):
        for j in range(len(even_numbers) - 1):
            if even_numbers[j] > even_numbers[j + 1]:
                even_numbers[j], even_numbers[j + 1] = even_numbers[j + 1], even_numbers[j]
    return even_numbers