"""
QUESTION:
Snuke has N integers: 1,2,\ldots,N. He will choose K of them and give those to Takahashi.

How many ways are there to choose K consecutive integers?

Constraints

* All values in input are integers.
* 1 \leq K \leq N \leq 50

Input

Input is given from Standard Input in the following format:


N K


Output

Print the answer.

Examples

Input

3 2


Output

2


Input

13 3


Output

11
"""

def count_ways_to_choose_consecutive_integers(N: int, K: int) -> int:
    """
    Calculates the number of ways to choose K consecutive integers from the range 1 to N.

    Parameters:
    - N (int): The total number of integers (1 to N).
    - K (int): The number of consecutive integers to choose.

    Returns:
    - int: The number of ways to choose K consecutive integers.
    """
    return N - K + 1