"""
QUESTION:
Create a function named `print_rhombus(n)` that prints a rhombus shape using asterisk (*) symbols. The function should take one integer argument `n`, representing the horizontal extent of the rhombus. If `n` is a negative number or a non-integer, the function should print an error message and return `None`. The rhombus should be centered and symmetrical about its middle line.
"""

def print_rhombus(n): 
    # Input validation
    try:
        # Check if the input is a negative number
        if n < 0:
            print("Entered value can't be negative.")
            return None
        # Check if the input is an integer
        elif not isinstance(n, int):
            print("Entered value should be an integer.")
            return None
    except TypeError:
        print("Input should be a numerical value.")
        return None
    
    # generate upper half of the rhombus
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # generate lower half of the rhombus
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))