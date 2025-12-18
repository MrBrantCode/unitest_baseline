"""
QUESTION:
Enter a positive integer n of 4,000 or less, with a pair of integers a, b, c, d in the range 0-1000.


a + b + c + d = n


Create a program that outputs the number of combinations that satisfy the conditions.



Input

Given multiple datasets. Each dataset is given n on one row. Please process until the end of the input.

The number of datasets does not exceed 50.

Output

For each data set, output the number of combinations of a, b, c, and d on one line.

Example

Input

2
3
35


Output

10
20
8436
"""

def count_combinations(n: int) -> int:
    """
    Counts the number of combinations of integers a, b, c, and d such that:
    a + b + c + d = n, where a, b, c, d are in the range 0-1000.

    Parameters:
    n (int): The sum of the four integers.

    Returns:
    int: The number of valid combinations.
    """
    return sum((max(0, min(i, 2002 - i)) * max(0, min(n - i + 2, 2000 - n + i)) for i in range(n + 2)))