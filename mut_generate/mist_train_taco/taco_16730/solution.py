"""
QUESTION:
Write a program which computes the digit number of sum of two integers a and b.

Constraints

* 0 ≤ a, b ≤ 1,000,000
* The number of datasets ≤ 200

Input

There are several test cases. Each test case consists of two non-negative integers a and b which are separeted by a space in a line. The input terminates with EOF.

Output

Print the number of digits of a + b for each data set.

Example

Input

5 7
1 99
1000 999


Output

2
3
4
"""

def calculate_sum_digit_count(a: int, b: int) -> int:
    """
    Computes the number of digits in the sum of two integers a and b.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The number of digits in the sum of a and b.
    """
    return len(str(a + b))