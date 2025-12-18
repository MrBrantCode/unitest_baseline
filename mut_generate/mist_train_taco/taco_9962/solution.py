"""
QUESTION:
In Aizu prefecture, we decided to create a new town to increase the population. To that end, we decided to cultivate a new rectangular land and divide this land into squares of the same size. The cost of developing this land is proportional to the number of plots, but the prefecture wants to minimize this cost.

Create a program to find the minimum maintenance cost for all plots, given the east-west and north-south lengths of the newly cultivated land and the maintenance cost per plot.



Input

The input is given in the following format.


W H C


The input is one line, the length W (1 ≤ W ≤ 1000) in the east-west direction and the length H (1 ≤ H ≤ 1000) in the north-south direction of the newly cultivated land, and the maintenance cost per plot C (1 ≤ 1000). C ≤ 1000) is given as an integer.

Output

Output the minimum cost required to maintain the land in one line.

Examples

Input

10 20 5


Output

10


Input

27 6 1


Output

18
"""

import math

def calculate_minimum_maintenance_cost(W, H, C):
    """
    Calculate the minimum maintenance cost for a rectangular land divided into plots.

    Parameters:
    W (int): The length in the east-west direction.
    H (int): The length in the north-south direction.
    C (int): The maintenance cost per plot.

    Returns:
    int: The minimum maintenance cost required to maintain the land.
    """
    g = math.gcd(W, H)
    return (W // g) * (H // g) * C