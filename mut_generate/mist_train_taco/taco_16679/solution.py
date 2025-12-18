"""
QUESTION:
Smeke has decided to participate in AtCoder Beginner Contest (ABC) if his current rating is less than 1200, and participate in AtCoder Regular Contest (ARC) otherwise.
You are given Smeke's current rating, x. Print ABC if Smeke will participate in ABC, and print ARC otherwise.

-----Constraints-----
 - 1 ≦ x ≦ 3{,}000
 - x is an integer.

-----Input-----
The input is given from Standard Input in the following format:
x

-----Output-----
Print the answer.

-----Sample Input-----
1000

-----Sample Output-----
ABC

Smeke's current rating is less than 1200, thus the output should be ABC.
"""

def determine_contest(x: int) -> str:
    """
    Determines which contest Smeke will participate in based on his current rating.

    Parameters:
    x (int): Smeke's current rating.

    Returns:
    str: 'ABC' if x < 1200, otherwise 'ARC'.
    """
    return 'ABC' if x < 1200 else 'ARC'