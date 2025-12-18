"""
QUESTION:
Shichi-Go-San (literally "Seven-Five-Three") is a traditional event in a certain country to celebrate the growth of seven-, five- and three-year-old children.
Takahashi is now X years old. Will his growth be celebrated in Shichi-Go-San this time?

-----Constraints-----
 - 1 ≤ X ≤ 9
 - X is an integer.

-----Input-----
Input is given from Standard Input in the following format:
X

-----Output-----
If Takahashi's growth will be celebrated, print YES; if it will not, print NO.

-----Sample Input-----
5

-----Sample Output-----
YES

The growth of a five-year-old child will be celebrated.
"""

def is_shichi_go_san_celebration(age: int) -> str:
    """
    Determines if Takahashi's growth will be celebrated in the Shichi-Go-San event.

    Parameters:
    age (int): The age of Takahashi.

    Returns:
    str: "YES" if the age is 3, 5, or 7, otherwise "NO".
    """
    if age in [3, 5, 7]:
        return "YES"
    else:
        return "NO"