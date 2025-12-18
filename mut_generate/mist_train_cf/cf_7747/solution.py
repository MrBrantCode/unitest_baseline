"""
QUESTION:
Write a function named `print_diamond` that takes an integer `rows` as input and prints a centered diamond pattern of '@' characters, with a space between each character, and an odd number of rows between 1 and 25. The function should validate the input and print an error message if the input is not a positive odd integer within the specified range.
"""

def print_diamond(rows):
    if rows < 1 or rows > 25 or rows % 2 == 0:
        print("Invalid input! Please enter a positive odd integer between 1 and 25.")
        return

    # Upper half of the diamond
    for i in range(rows // 2 + 1):
        spaces = " " * (rows // 2 - i)
        asterisks = "@" * (2 * i + 1)
        print(spaces + asterisks + spaces)

    # Lower half of the diamond
    for i in range(rows // 2 - 1, -1, -1):
        spaces = " " * (rows // 2 - i)
        asterisks = "@" * (2 * i + 1)
        print(spaces + asterisks + spaces)