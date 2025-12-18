"""
QUESTION:
An elementary school student Takahashi has come to a variety store.
He has two coins, A-yen and B-yen coins (yen is the currency of Japan), and wants to buy a toy that costs C yen. Can he buy it?
Note that he lives in Takahashi Kingdom, and may have coins that do not exist in Japan.

-----Constraints-----
 - All input values are integers.
 - 1 \leq A, B \leq 500
 - 1 \leq C \leq 1000

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
If Takahashi can buy the toy, print Yes; if he cannot, print No.

-----Sample Input-----
50 100 120

-----Sample Output-----
Yes

He has 50 + 100 = 150 yen, so he can buy the 120-yen toy.
"""

def can_takahashi_buy_toy(A: int, B: int, C: int) -> str:
    """
    Determines if Takahashi can buy a toy with the given coins.

    Parameters:
    - A (int): The value of the first coin.
    - B (int): The value of the second coin.
    - C (int): The cost of the toy.

    Returns:
    - str: "Yes" if Takahashi can buy the toy, "No" otherwise.
    """
    return "Yes" if A + B >= C else "No"