"""
QUESTION:
If you draw a few infinitely long straight lines on an infinitely wide plane, this plane will be divided into several areas. For example, if you draw a straight line, the plane will be divided into two areas. Even if you draw the same number of straight lines, the number of areas obtained will differ depending on how you draw. For example, if you draw two straight lines in parallel, you get three areas, and if you draw two straight lines perpendicular to each other, you get four areas.

<image>


Create a program that outputs the maximum number of regions that can be obtained by drawing n straight lines.



Input

Given multiple datasets. Each dataset is given n (1 ≤ n ≤ 10,000) on one row. Please process until the end of the input.

The number of datasets does not exceed 50.

Output

For each dataset, output the maximum number of divisions on one line.

Example

Input

1
3


Output

2
7
"""

def calculate_max_regions(n: int) -> int:
    """
    Calculate the maximum number of regions that can be obtained by drawing n straight lines on an infinitely wide plane.

    Parameters:
    n (int): The number of straight lines to be drawn.

    Returns:
    int: The maximum number of regions.
    """
    ans = 0.5 * n * n + 0.5 * n + 1
    return round(ans)