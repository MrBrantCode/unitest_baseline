"""
QUESTION:
In some other world, today is the day before Christmas Eve.
Mr. Takaha is buying N items at a department store. The regular price of the i-th item (1 \leq i \leq N) is p_i yen (the currency of Japan).
He has a discount coupon, and can buy one item with the highest price for half the regular price. The remaining N-1 items cost their regular prices. What is the total amount he will pay?

-----Constraints-----
 - 2 \leq N \leq 10
 - 100 \leq p_i \leq 10000
 - p_i is an even number.

-----Input-----
Input is given from Standard Input in the following format:
N
p_1
p_2
:
p_N

-----Output-----
Print the total amount Mr. Takaha will pay.

-----Sample Input-----
3
4980
7980
6980

-----Sample Output-----
15950

The 7980-yen item gets the discount and the total is 4980 + 7980 / 2 + 6980 = 15950 yen.
Note that outputs such as 15950.0 will be judged as Wrong Answer.
"""

def calculate_total_payment(prices):
    """
    Calculate the total amount Mr. Takaha will pay after applying a discount coupon.

    Parameters:
    prices (list of int): A list of integers representing the regular prices of the items.

    Returns:
    int: The total amount Mr. Takaha will pay after applying the discount.
    """
    if len(prices) < 2:
        raise ValueError("The number of items must be at least 2.")
    
    highest_price = max(prices)
    total_payment = sum(prices) - highest_price // 2
    
    return total_payment