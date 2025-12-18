"""
QUESTION:
Find places where a string P is found within a text T. Print all indices of T where P found. The indices of T start with 0.

Constraints

* 1 ≤ length of T ≤ 1000000
* 1 ≤ length of P ≤ 10000
* The input consists of alphabetical characters and digits

Input

In the first line, a text T is given. In the second line, a string P is given.

Output

Print an index of T where P found in a line. Print the indices in ascending order.

Examples

Input

aabaaa
aa


Output

0
3
4


Input

xyzz
yz


Output

1


Input

abc
xyz


Output
"""

def find_pattern_indices(T: str, P: str) -> list[int]:
    """
    Finds all starting indices of the pattern P within the text T.

    Parameters:
    - T (str): The text string in which to search for the pattern.
    - P (str): The pattern string to search for within T.

    Returns:
    - list[int]: A list of integers representing the starting indices of P within T.
    """
    indices = []
    for x in range(len(T) - len(P) + 1):
        if T[x:x + len(P)] == P:
            indices.append(x)
    return indices