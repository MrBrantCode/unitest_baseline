"""
QUESTION:
Design a function `print_diamond(n, char)` that prints a diamond shape of a given width `n` and character `char`. The function should handle both even and odd widths and validate the input parameters. Additionally, create a function `print_execution_time(print_diamond_func, n, char)` that prints the execution time of the `print_diamond` function. The solution should have a complexity of O(n). The input parameters `n` and `char` should be validated to ensure `n` is a positive integer and `char` is a single character.
"""

def diamond(n, char):
    """
    Prints a diamond shape of a given width `n` and character `char`.
    
    Args:
        n (int): The width of the diamond shape.
        char (str): The character to use for the diamond shape.
    
    Returns:
        None
    """
    if n <= 0 or not isinstance(n, int):
        return 'Error: Invalid size.'
    if len(char) != 1:
        return 'Error: Invalid character.'

    for i in range(n):
        print(' ' * (n - i - 1) + char * (2*i+1))
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + char * (2*i+1))