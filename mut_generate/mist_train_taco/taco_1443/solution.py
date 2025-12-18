"""
QUESTION:
You're given an integer N. Write a program to calculate the sum of all the digits of N. 

-----Input-----

The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N. 

-----Output-----
For each test case, calculate the sum of digits of N, and display it in a new line.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000

-----Example-----
Input
3 
12345
31203
2123
Output
15
9
8
"""

def sum_of_digits(N: int) -> int:
    """
    Calculate the sum of all the digits of the given integer N.

    Parameters:
    N (int): The integer whose digits are to be summed.

    Returns:
    int: The sum of the digits of N.
    """
    sum_of_digits = 0
    while N > 0:
        sum_of_digits += N % 10
        N //= 10
    return sum_of_digits