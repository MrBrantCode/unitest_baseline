"""
QUESTION:
La Confiserie d'ABC sells cakes at 4 dollars each and doughnuts at 7 dollars each.
Determine if there is a way to buy some of them for exactly N dollars. You can buy two or more doughnuts and two or more cakes, and you can also choose to buy zero doughnuts or zero cakes.

-----Constraints-----
 - N is an integer between 1 and 100, inclusive.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If there is a way to buy some cakes and some doughnuts for exactly N dollars, print Yes; otherwise, print No.

-----Sample Input-----
11

-----Sample Output-----
Yes

If you buy one cake and one doughnut, the total will be 4 + 7 = 11 dollars.
"""

def can_buy_cakes_and_doughnuts(N: int) -> str:
    """
    Determines if it is possible to buy cakes and doughnuts for exactly N dollars.

    Parameters:
    - N (int): The total amount of money in dollars that needs to be spent exactly.

    Returns:
    - str: "Yes" if it is possible to buy cakes and doughnuts for exactly N dollars, otherwise "No".
    """
    for i in range(26):  # Since 4 * 25 = 100, the maximum number of cakes we need to consider is 25
        for j in range(16):  # Since 7 * 14 = 98, the maximum number of doughnuts we need to consider is 14
            if 4 * i + 7 * j == N:
                return "Yes"
    return "No"