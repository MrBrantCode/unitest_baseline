"""
QUESTION:
Write a function `calculate_even_sum` that calculates the sum of unique even numbers in a given list. The list may contain non-numeric elements and duplicates. The function should ignore non-numeric elements and only consider the first occurrence of each even number. If the list is empty, the function should return 0.
"""

def calculate_even_sum(lst):
    """
    Calculates the sum of unique even numbers in a given list.

    Args:
        lst (list): A list containing numeric and non-numeric elements.

    Returns:
        int: The sum of unique even numbers in the list.
    """
    even_sum = 0
    seen_even_numbers = set()
    
    for num in lst:
        if isinstance(num, int) and num % 2 == 0 and num not in seen_even_numbers:
            even_sum += num
            seen_even_numbers.add(num)
    
    return even_sum