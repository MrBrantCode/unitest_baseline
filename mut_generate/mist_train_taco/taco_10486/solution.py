"""
QUESTION:
Remainder of Big Integers

Given two integers $A$ and $B$, compute the remainder of $\frac{A}{B}$.

Input

Two integers $A$ and $B$ separated by a space character are given in a line.

Output

Print the remainder in a line.

Constraints

* $0 \leq A, B \leq 10^{1000}$
* $B \ne 0$



Sample Input 1


5 8


Sample Output 1


5


Sample Input 2


100 25


Sample Output 2


0






Example

Input

5 8


Output

5
"""

def compute_remainder(A: int, B: int) -> int:
    """
    Compute the remainder of the division of A by B.

    Parameters:
    A (int): The dividend.
    B (int): The divisor.

    Returns:
    int: The remainder of the division of A by B.
    """
    return A % B