"""
QUESTION:
Write a function called `print_table(number, range_)` that prints a multiplication table of a given number 'number' up to a given range 'range_'. The function should print the table in a formatted manner with the products aligned in columns. Implement error handling for negative numbers and non-integer inputs. The function should take two parameters: 'number' and 'range_', both of which are integers.
"""

def print_table(number, range_):
    # Error handling for negative numbers and non-integer inputs
    if not isinstance(number, int) or not isinstance(range_, int):
        print("Error: Please enter integer values for number and range.")
        return

    if number < 0 or range_ < 0:
        print("Error: Please enter non-negative values for number and range.")
        return

    # Print the multiplication table
    for i in range(1, range_ + 1):
        print(f"{number} x {i} = {number * i}")