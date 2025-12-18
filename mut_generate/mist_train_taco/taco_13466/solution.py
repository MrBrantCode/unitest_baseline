"""
QUESTION:
problem

Taro often shop at JOI general stores. At JOI general stores, there are enough coins of 500 yen, 100 yen, 50 yen, 10 yen, 5 yen, and 1 yen, and we always pay the change so that the number of coins is the smallest. Create a program to find the number of coins included in the change you receive when Taro goes shopping at the JOI general store and puts out one 1000 yen bill at the cash register.

For example, in the case of input example 1, 4 must be output as shown in the figure below.

<image>



input

The input consists of multiple datasets. Each dataset consists of one line, and only one amount (an integer of 1 or more and less than 1000) paid by Taro is written. The input data ends with one zero line.

The number of datasets does not exceed 5.

output

Output the number of coins included in the change for each dataset on one line.

Examples

Input

380
1
0


Output

4
15


Input

None


Output

None
"""

def calculate_minimum_coins(amount_paid: int) -> int:
    """
    Calculate the minimum number of coins included in the change when Taro pays with a 1000 yen bill.

    Parameters:
    - amount_paid (int): The amount paid by Taro, which is an integer between 1 and 999 (inclusive).

    Returns:
    - int: The number of coins included in the change.
    """
    change = 1000 - amount_paid
    
    coins = [500, 100, 50, 10, 5, 1]
    coin_count = 0
    
    for coin in coins:
        coin_count += change // coin
        change %= coin
    
    return coin_count