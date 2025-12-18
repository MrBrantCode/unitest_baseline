"""
QUESTION:
How many multiples of d are there among the integers between L and R (inclusive)?

Constraints

* All values in input are integers.
* 1 \leq L \leq R \leq 100
* 1 \leq d \leq 100

Input

Input is given from Standard Input in the following format:


L R d


Output

Print the number of multiples of d among the integers between L and R (inclusive).

Examples

Input

5 10 2


Output

3


Input

6 20 7


Output

2


Input

1 100 1


Output

100
"""

def count_multiples_in_range(L: int, R: int, d: int) -> int:
    """
    Counts the number of multiples of `d` between `L` and `R` (inclusive).

    Parameters:
    - L (int): The lower bound of the range (inclusive).
    - R (int): The upper bound of the range (inclusive).
    - d (int): The divisor to check for multiples.

    Returns:
    - int: The number of multiples of `d` between `L` and `R` (inclusive).
    """
    return R // d - (L - 1) // d