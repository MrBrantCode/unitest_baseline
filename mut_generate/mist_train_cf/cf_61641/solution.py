"""
QUESTION:
Create a function named `print_sequence` that prints a sequence of integers from 0 to the input number (inclusive) using a 'for' loop. The function should handle potential errors, such as non-integer or string inputs, and not crash if an error occurs. The function should print an error message if a non-integer input is detected or if any other general error occurs.
"""

def print_sequence(n):
    """
    Prints a sequence of integers from 0 to the input number (inclusive) using a 'for' loop.
    
    Args:
    n (int): The upper limit of the sequence.
    
    Returns:
    None
    """
    try:
        if not isinstance(n, int):
            print("Error: Input is not an integer.")
            return
        for i in range(n + 1):
            print(i)
    except Exception as e:
        print("An error occurred: ", e)