"""
QUESTION:
M-kun is a competitor in AtCoder, whose highest rating is X.
In this site, a competitor is given a kyu (class) according to his/her highest rating. For ratings from 400 through 1999, the following kyus are given:

* From 400 through 599: 8-kyu
* From 600 through 799: 7-kyu
* From 800 through 999: 6-kyu
* From 1000 through 1199: 5-kyu
* From 1200 through 1399: 4-kyu
* From 1400 through 1599: 3-kyu
* From 1600 through 1799: 2-kyu
* From 1800 through 1999: 1-kyu



What kyu does M-kun have?

Constraints

* 400 \leq X \leq 1999
* X is an integer.

Input

Input is given from Standard Input in the following format:


X


Output

Print the kyu M-kun has, as an integer. For example, if he has 8-kyu, print `8`.

Examples

Input

725


Output

7


Input

1600


Output

2
"""

def determine_kyu(X: int) -> int:
    """
    Determine the kyu corresponding to the given highest rating X.

    Parameters:
    X (int): The highest rating of M-kun.

    Returns:
    int: The kyu corresponding to the rating X.
    """
    return 8 - (X - 400) // 200