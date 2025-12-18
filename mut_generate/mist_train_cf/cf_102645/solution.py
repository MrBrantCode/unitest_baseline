"""
QUESTION:
Write a function named `print_2d_array` that takes a 2D array as input. The function should print each row of the 2D array on a new line, with elements separated by a space. If the input array is empty, the function should print "Empty array." If the input array contains non-integer elements, the function should print "Invalid input: array contains non-integer elements."
"""

def print_2d_array(arr):
    """
    Prints each row of the 2D array on a new line, with elements separated by a space.
    
    Args:
        arr (list): A 2D array containing integers.
    
    Returns:
        None
    """
    if len(arr) == 0:
        print("Empty array.")
        return

    for row in arr:
        for element in row:
            if type(element) != int:
                print("Invalid input: array contains non-integer elements.")
                return
            print(element, end=" ")
        print()