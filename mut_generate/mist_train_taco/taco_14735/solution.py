"""
QUESTION:
<image> <image>

*The two images are equivalent, feel free to use either one.

Input

The input contains a single integer a (-100 ≤ a ≤ 100).

Output

Output the result – an integer number.

Example

Input


1


Output


1
"""

def calculate_result(a: int) -> int:
    """
    Calculate the result based on the given integer a.

    Parameters:
    a (int): An integer within the range -100 to 100.

    Returns:
    int: The result of the calculation 2 - a^2.
    """
    return 2 - a ** 2