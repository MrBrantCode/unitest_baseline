"""
QUESTION:
A frog is about to return to the burrow. The burrow is D centimeters ahead of the frog, and the frog goes straight toward the burrow. There are only two actions that a frog can do:

* Large jump (go forward L centimeters)
* Small jump (go 1 cm forward)



The frog aims to just land in the burrow without jumping over it.

Create a program that asks how many times a frog needs to jump to return to its burrow.



Input

The input is given in the following format.


DL


The input is one line, given the distance D (1 ≤ D ≤ 10000) to the burrow and the distance L (2 ≤ L ≤ 10000) for the frog to travel on a large jump.

Output

Print on one line how many times the frog needs to jump.

Examples

Input

10 5


Output

2


Input

7 4


Output

4
"""

def calculate_frog_jumps(D: int, L: int) -> int:
    """
    Calculate the number of jumps a frog needs to reach its burrow.

    Parameters:
    D (int): The distance to the burrow.
    L (int): The distance the frog travels on a large jump.

    Returns:
    int: The number of jumps required.
    """
    return D // L + D % L