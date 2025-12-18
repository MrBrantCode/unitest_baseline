"""
QUESTION:
Create a function named `print_zigzag_asterisks(n)` that prints a zigzag pattern of asterisk characters, where n is the number of rows and the number of asterisks in each even row. In odd rows, the asterisk should be at the end, preceded by n-1 spaces. If n is less than 1, the function should not print anything.
"""

def print_zigzag_asterisks(n):
    if n < 1:
        return
    
    for row in range(n):
        if row % 2 == 0:
            print('*' * n)  
        else:
            print(' ' * (n-1) + '*')