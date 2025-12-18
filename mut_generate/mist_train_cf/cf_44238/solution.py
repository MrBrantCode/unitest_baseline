"""
QUESTION:
Create a function `progressive_accumulation` that takes a list of numbers as input and returns the intermediate subtotals of the progressive accumulation of the numerical values in the list. The function should return a list of subtotals, where each subtotal is the sum of all numbers up to that point in the list.
"""

def progressive_accumulation(numbers):
    """
    Calculate the intermediate subtotals of the progressive accumulation of the numerical values in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of subtotals, where each subtotal is the sum of all numbers up to that point in the list.
    """
    subtotals = []
    total = 0
    for num in numbers:
        total += num
        subtotals.append(total)
    return subtotals