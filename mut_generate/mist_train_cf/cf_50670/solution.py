"""
QUESTION:
Create a recursive function `print_string` that takes two parameters: an integer `m` and a string `string`. The function should print the `string` exactly `m` times. If `m` is less than or equal to 0, the function should stop printing.
"""

def entrance(m, string):
    # Base case: if m is less than or equal to 0, stop recursion
    if m <= 0:
        return
    else:
        # Print the string
        print(string)
        # Recursive call, reduce m by 1
        entrance(m - 1, string)