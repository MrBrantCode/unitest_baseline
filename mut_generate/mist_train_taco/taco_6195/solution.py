"""
QUESTION:
Write a program which reads two integers x and y, and prints them in ascending order.

Constraints

* 0 ≤ x, y ≤ 10000
* the number of datasets ≤ 3000

Input

The input consists of multiple datasets. Each dataset consists of two integers x and y separated by a single space.

The input ends with two 0 (when both x and y are zero). Your program should not process for these terminal symbols.

Output

For each dataset, print x and y in ascending order in a line. Put a single space between x and y.

Example

Input

3 2
2 2
5 3
0 0


Output

2 3
2 2
3 5
"""

def sort_two_integers(x: int, y: int) -> tuple:
    """
    Sorts two integers in ascending order and returns them as a tuple.

    Parameters:
    - x (int): The first integer.
    - y (int): The second integer.

    Returns:
    - tuple: A tuple containing the two integers in ascending order.
    """
    return tuple(sorted((x, y)))