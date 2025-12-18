"""
QUESTION:
Aoki is in search of Takahashi, who is missing in a one-dimentional world. Initially, the coordinate of Aoki is 0, and the coordinate of Takahashi is known to be x, but his coordinate afterwards cannot be known to Aoki.

Time is divided into turns. In each turn, Aoki and Takahashi take the following actions simultaneously:

* Let the current coordinate of Aoki be a, then Aoki moves to a coordinate he selects from a-1, a and a+1.

* Let the current coordinate of Takahashi be b, then Takahashi moves to the coordinate b-1 with probability of p percent, and moves to the coordinate b+1 with probability of 100-p percent.




When the coordinates of Aoki and Takahashi coincide, Aoki can find Takahashi. When they pass by each other, Aoki cannot find Takahashi.

Aoki wants to minimize the expected number of turns taken until he finds Takahashi. Find the minimum possible expected number of turns.

Constraints

* 1 ≦ x ≦ 1,000,000,000
* 1 ≦ p ≦ 100
* x and p are integers.

Input

The input is given from Standard Input in the following format:


x
p


Output

Print the minimum possible expected number of turns. The output is considered correct if the absolute or relative error is at most 10^{-6}.

Examples

Input

3
100


Output

2.0000000


Input

6
40


Output

7.5000000


Input

101
80


Output

63.7500000
"""

import math

def calculate_minimum_expected_turns(x: int, p: float) -> float:
    """
    Calculate the minimum possible expected number of turns for Aoki to find Takahashi.

    Parameters:
    x (int): The initial coordinate of Takahashi.
    p (float): The probability (in percentage) that Takahashi moves to the left.

    Returns:
    float: The minimum possible expected number of turns, with an absolute or relative error of at most 10^-6.
    """
    p = p / 100  # Convert percentage to a decimal
    return math.ceil(x / 2) / p