"""
QUESTION:
Notes

For this problem, it is recommended to use floating point numbers, which are more accurate than double.



Input


m n x
k l y


For input, six integers m, n, x, k, l, y are given in the above input format.
These six integers correspond to those in the problem statement, repeating the horizontal m: n cut x times and the vertical k: l cut y times.
1 ≤ m, n, k, l ≤ 100, 0 ≤ x, y ≤ 40, and m, n and l, k are relatively prime.

Output

Print out the expected number of planarians that are regenerating to their original form after a few weeks in a row.
The output is acceptable with an error of 10-6 or less.

Examples

Input

1 1 1
1 1 1


Output

0.562500


Input

1 2 2
1 1 1


Output

0.490741


Input

1 2 0
3 4 0


Output

1.000000
"""

def calculate_expected_planarians(m: int, n: int, x: int, k: int, l: int, y: int) -> float:
    """
    Calculate the expected number of planarians that are regenerating to their original form
    after a few weeks in a row.

    Parameters:
    m (int): The first integer for the horizontal cut.
    n (int): The second integer for the horizontal cut.
    x (int): The number of times the horizontal cut is repeated.
    k (int): The first integer for the vertical cut.
    l (int): The second integer for the vertical cut.
    y (int): The number of times the vertical cut is repeated.

    Returns:
    float: The expected number of planarians regenerating to their original form, with an error of 10^-6 or less.
    """
    horizontal_part = 0.5 * (1.0 + (m ** 2 + n ** 2) ** x / (m + n) ** (2 * x))
    vertical_part = 0.5 * (1.0 + (k ** 2 + l ** 2) ** y / (k + l) ** (2 * y))
    return horizontal_part * vertical_part