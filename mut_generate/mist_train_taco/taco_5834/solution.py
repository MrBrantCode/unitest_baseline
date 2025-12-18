"""
QUESTION:
We will buy a product for N yen (the currency of Japan) at a shop.
If we use only 1000-yen bills to pay the price, how much change will we receive?
Assume we use the minimum number of bills required.

-----Constraints-----
 - 1 \leq N \leq 10000
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the amount of change as an integer.

-----Sample Input-----
1900

-----Sample Output-----
100

We will use two 1000-yen bills to pay the price and receive 100 yen in change.
"""

def calculate_change(N: int) -> int:
    """
    Calculate the amount of change received when paying for a product priced at N yen
    using only 1000-yen bills. The change is the difference between the total amount
    paid and the price, considering the minimum number of 1000-yen bills used.

    Parameters:
    - N (int): The price of the product in yen.

    Returns:
    - int: The amount of change in yen.
    """
    return (1000 - N % 1000) % 1000