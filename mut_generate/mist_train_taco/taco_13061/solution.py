"""
QUESTION:
Write a program which reads an integer and prints sum of its digits.



Input

The input consists of multiple datasets. For each dataset, an integer x is given in a line. The number of digits in x does not exceed 1000.

The input ends with a line including single zero. Your program should not process for this terminal symbol.

Output

For each dataset, print the sum of digits in x.

Example

Input

123
55
1000
0


Output

6
10
1
"""

def sum_of_digits(x: str) -> int:
    """
    Calculate the sum of the digits of the given integer represented as a string.

    Parameters:
    x (str): A string representing the integer whose digits need to be summed.

    Returns:
    int: The sum of the digits of the input string.
    """
    return sum(int(digit) for digit in x)