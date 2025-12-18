"""
QUESTION:
Create a function `perform_operations` that takes a list of numbers and performs the following operations on each number: add 2, divide by 2, multiply by 3, subtract 4, and square the number. The function should handle division by zero and other potential exceptions, printing an error message if an exception occurs. The function should return the results of the operations for each number in the list. 

Restrictions: The function should handle cases where the input list is empty or contains zero. The division by zero operation should return "undefined".
"""

def perform_operations(numbers):
    """
    Performs operations on a list of numbers: add 2, divide by 2, multiply by 3, subtract 4, and square the number.
    Handles division by zero and other potential exceptions.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of lists containing the results of the operations for each number.
    """
    results = []
    for a in numbers:
        try:
            b = [a+2, a/2 if a != 0 else "undefined", a*3, a-4, a**2]
            results.append(b)
        except Exception as e:
            print("Unexpected error: " + str(e))
    return results