"""
QUESTION:
Our master carpenter is designing a condominium called Bange Hills Mansion. The condominium is constructed by stacking up floors of the same height. The height of each floor is designed so that the total height of the stacked floors coincides with the predetermined height of the condominium. The height of each floor can be adjusted freely with a certain range.

The final outcome of the building depends on clever height allotment for each floor. So, he plans to calculate possible combinations of per-floor heights to check how many options he has.

Given the height of the condominium and the adjustable range of each floor’s height, make a program to enumerate the number of choices for a floor.



Input

The input is given in the following format.


$H$ $A$ $B$


The input line provides the height of the condominium $H$ ($1 \leq H \leq 10^5$) and the upper and lower limits $A$ and $B$ of the height adjustable range for one floor ($1 \leq A \leq B \leq H$). All data are given as integers.

Output

Output the number of possible height selections for each floor in a line.

Examples

Input

100 2 4


Output

2


Input

101 3 5


Output

0
"""

def count_floor_height_combinations(H: int, A: int, B: int) -> int:
    """
    Counts the number of possible height selections for each floor such that the total height of the condominium is exactly H.

    Parameters:
    - H (int): The height of the condominium.
    - A (int): The lower limit of the height adjustable range for one floor.
    - B (int): The upper limit of the height adjustable range for one floor.

    Returns:
    - int: The number of possible height selections for each floor.
    """
    ans = 0
    for k in range(A, B + 1):
        if H % k == 0:
            ans += 1
    return ans