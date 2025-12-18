"""
QUESTION:
Create a function named `staircase_pattern` that generates a staircase pattern. The function should have two parameters: `n` and `char`. `n` is a required parameter that must be a positive integer, representing the number of stairs in the staircase. `char` is an optional parameter that must be a single character string, representing the character used to build the stairs. If `char` is not provided, the function should use '*' by default. The function should handle invalid inputs, such as non-integer or non-positive values for `n`, and non-string or multiple-character values for `char`, by printing an error message and returning without further action. The function should also handle non-printable characters by catching the `UnicodeEncodeError` and printing a corresponding error message.
"""

def staircase_pattern(n, char='*'):
    # Check if n is non-integer or smaller than 1
    if not isinstance(n, int) or n < 1:
        print("Invalid input! Please input a positive integer.")
        return
    # Check if char is not a string or has multiple characters
    elif not isinstance(char, str) or len(char) != 1:
        print("Invalid input! Please input a single character.")
        return
    try:
        # Print staircase pattern
        for i in range(n):
            print(' ' * (n - i - 1) + char * (i + 1))
    except UnicodeEncodeError:
        print('Unable to print using the provided character.')
        return