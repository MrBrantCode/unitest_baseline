"""
QUESTION:
Polycarp plays a well-known computer game (we won't mention its name). In this game, he can craft tools of two types — shovels and swords. To craft a shovel, Polycarp spends two sticks and one diamond; to craft a sword, Polycarp spends two diamonds and one stick.

Each tool can be sold for exactly one emerald. How many emeralds can Polycarp earn, if he has $a$ sticks and $b$ diamonds?


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases.

The only line of each test case contains two integers $a$ and $b$ ($0 \le a, b \le 10^9$) — the number of sticks and the number of diamonds, respectively.


-----Output-----

For each test case print one integer — the maximum number of emeralds Polycarp can earn.


-----Example-----
Input
4
4 4
1000000000 0
7 15
8 7

Output
2
0
7
5



-----Note-----

In the first test case Polycarp can earn two emeralds as follows: craft one sword and one shovel.

In the second test case Polycarp does not have any diamonds, so he cannot craft anything.
"""

import math

def max_emeralds(a: int, b: int) -> int:
    """
    Calculate the maximum number of emeralds Polycarp can earn given the number of sticks and diamonds.

    Parameters:
    a (int): The number of sticks.
    b (int): The number of diamonds.

    Returns:
    int: The maximum number of emeralds Polycarp can earn.
    """
    c = max(a, b)
    d = min(a, b)
    
    if c >= 2 * d:
        return d
    else:
        x = math.ceil((2 * d - c) / 3)
        d -= x * 2
        return x + d