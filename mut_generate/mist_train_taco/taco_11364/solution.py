"""
QUESTION:
Takahashi has K 500-yen coins. (Yen is the currency of Japan.)
If these coins add up to X yen or more, print Yes; otherwise, print No.

-----Constraints-----
 - 1 \leq K \leq 100
 - 1 \leq X \leq 10^5

-----Input-----
Input is given from Standard Input in the following format:
K X

-----Output-----
If the coins add up to X yen or more, print Yes; otherwise, print No.

-----Sample Input-----
2 900

-----Sample Output-----
Yes

Two 500-yen coins add up to 1000 yen, which is not less than X = 900 yen.
"""

def can_afford_with_500_yen_coins(K: int, X: int) -> str:
    """
    Determines if the total value of K 500-yen coins is at least X yen.

    Parameters:
    - K (int): Number of 500-yen coins.
    - X (int): Total amount of yen required.

    Returns:
    - str: "Yes" if the total value of the coins is at least X, otherwise "No".
    """
    return 'Yes' if 500 * K >= X else 'No'