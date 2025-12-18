"""
QUESTION:
Accepts a string from the user and print the reverse string as the output without using any built-in function.

-----Input:-----
Each testcase contains of a single line of input, a string.

-----Output:-----
For each testcase, output in a single line answer, the reverse string.

-----Sample Input:-----
1
Tracy

-----Sample Output:-----
ycarT
"""

def reverse_string(input_string: str) -> str:
    """
    Reverses the input string without using any built-in functions.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed version of the input string.
    """
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string