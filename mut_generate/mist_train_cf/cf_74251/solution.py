"""
QUESTION:
Implement a function named `square_numbers` that uses a while loop to iterate through a given list of numbers, squares each number, and stores the result in a new list. The function should handle potential exceptions by printing an error message if the list contains a non-numeric value. The input list is not guaranteed to contain only numbers.
"""

def square_numbers(arr):
    """
    Squares numbers in a given list and stores the result in a new list.
    
    Handles potential exceptions by printing an error message if the list contains a non-numeric value.

    Args:
        arr (list): A list of numbers.

    Returns:
        list: A list of squared numbers.
    """
    result = []
    i = 0
    while i < len(arr):
        try:
            result.append(arr[i]**2)
        except TypeError:
            print(f"Error: {arr[i]} is not a number and cannot be squared.")
        finally:
            i += 1
    return result