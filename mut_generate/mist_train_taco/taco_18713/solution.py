"""
QUESTION:
You went shopping to buy cakes and donuts with X yen (the currency of Japan).
First, you bought one cake for A yen at a cake shop.
Then, you bought as many donuts as possible for B yen each, at a donut shop.
How much do you have left after shopping?

-----Constraints-----
 - 1 \leq A, B \leq 1 000
 - A + B \leq X \leq 10 000
 - X, A and B are integers.

-----Input-----
Input is given from Standard Input in the following format:
X
A
B

-----Output-----
Print the amount you have left after shopping.

-----Sample Input-----
1234
150
100

-----Sample Output-----
84

You have 1234 - 150 = 1084 yen left after buying a cake.
With this amount, you can buy 10 donuts, after which you have 84 yen left.
"""

def calculate_remaining_yen(X: int, A: int, B: int) -> int:
    """
    Calculate the amount of yen left after buying one cake and as many donuts as possible.

    Parameters:
    X (int): The total amount of yen available.
    A (int): The cost of one cake in yen.
    B (int): The cost of one donut in yen.

    Returns:
    int: The amount of yen left after shopping.
    """
    remaining_after_cake = X - A
    remaining_after_donuts = remaining_after_cake % B
    return remaining_after_donuts