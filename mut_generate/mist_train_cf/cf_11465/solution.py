"""
QUESTION:
Create a function named `print_zigzag_asterisks` that takes an integer `n` as input and prints `n` asterisk characters in a zigzag pattern, with `n` asterisks in each even row and `n-1` spaces followed by an asterisk in each odd row. The function should not print anything if `n` is less than 1.
"""

def print_zigzag_asterisks(n):
    # Check if n is less than 1, then return without printing anything
    if n < 1:
        return
    
    # Loop through each row
    for row in range(n):
        # Print asterisk characters in zigzag pattern
        if row % 2 == 0:
            print('*' * n)  # Print n asterisks in a row
        else:
            print(' ' * (n-1) + '*')  # Print a space followed by an asterisk at the end