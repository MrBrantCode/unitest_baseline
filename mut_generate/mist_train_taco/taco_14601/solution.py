"""
QUESTION:
Addition of Big Integers

Given two integers $A$ and $B$, compute the sum, $A + B$.

Input

Two integers $A$ and $B$ separated by a space character are given in a line.

Output

Print the sum in a line.

Constraints

* $-1 \times 10^{100000} \leq A, B \leq 10^{100000}$



Sample Input 1


5 8


Sample Output 1


13


Sample Input 2


100 25


Sample Output 2


125


Sample Input 3


-1 1


Sample Output 3


0


Sample Input 4


12 -3


Sample Output 4


9






Example

Input

5 8


Output

13
"""

def add_big_integers(A: int, B: int) -> int:
    """
    Adds two large integers A and B.

    Parameters:
    A (int): The first integer.
    B (int): The second integer.

    Returns:
    int: The sum of A and B.
    """
    return A + B