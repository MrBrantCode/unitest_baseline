"""
QUESTION:
Oranges on Cans

square1001 You put a $ N $ can of aluminum on the table.

E869120 You put $ M $ of oranges on each aluminum can on the table.

How many oranges are on the aluminum can?

input

Input is given from standard input in the following format.


$ N $ $ M $


output

Output the number of oranges on the aluminum can in one line.

However, insert a line break at the end.

Constraint

* $ 1 \ leq N \ leq 9 $
* $ 1 \ leq M \ leq 9 $
* All inputs are integers.



Input example 1


3 4


Output example 1


12


Input example 2


7 7


Output example 2


49






Example

Input

3 4


Output

12
"""

def calculate_total_oranges(N: int, M: int) -> int:
    """
    Calculate the total number of oranges on the cans.

    Parameters:
    N (int): Number of cans.
    M (int): Number of oranges per can.

    Returns:
    int: Total number of oranges.
    """
    return N * M