"""
QUESTION:
Create a function called `print_diamond(rows)` that prints a centered diamond pattern to the console. The function should take an integer `rows` as input, representing the number of rows in the diamond. The function must validate the input to ensure that `rows` is a positive odd integer. If the input is invalid, the function should print an error message and exit. The diamond pattern should have a space between each asterisk and each row should be centered. The function should not return any value. The input `rows` should be obtained from the user.
"""

def print_diamond(rows):
    if rows % 2 == 0 or rows < 1:
        print("Number of rows must be a positive odd integer.")
        return

    for i in range(1, rows + 1, 2):
        print(" " * ((rows - i) // 2) + "*" * i)

    for i in range(rows - 2, 0, -2):
        print(" " * ((rows - i) // 2) + "*" * i)