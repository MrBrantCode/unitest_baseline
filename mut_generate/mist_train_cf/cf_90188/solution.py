"""
QUESTION:
Write a function named `reverse_print_odd` that takes an array of strings as input. The function should print the elements of the array in reverse order, but only include elements with an odd number of characters. Implement the function using recursion and include error handling for any unexpected errors that may occur during execution.
"""

def reverse_print_odd(arr):
    """
    Recursively print elements of the array in reverse order, 
    but only include elements with an odd number of characters.

    Args:
        arr (list): A list of strings.
    """
    # Base case: If the array is empty, return
    if len(arr) == 0:
        return

    # Recursive case: Print the last element if it has an odd number of characters
    if len(arr[-1]) % 2 != 0:
        print(arr[-1])

    # Recursive call with the remaining elements of the array
    reverse_print_odd(arr[:-1])