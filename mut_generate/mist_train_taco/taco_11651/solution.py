"""
QUESTION:
Apples and Oranges. You thought this question was gone when you passed class 6th. WELL YOU ARE WRONG. It's back.

See we have n apples and m oranges. You need to put these apples and oranges into some boxes. Though we've put some terms&conditions with a bright *

1. Number of apples should be same in each box.

2. Number of oranges should be same in each box

3. Number of boxes should be greatest under the above two conditions

Input

First line contains n & m, two integers. n lies in 1 to 10^9. m lies in 1 to 10^9
Output
Number of apples and oranges in each box

Sample Input

12028 12772

Sample Output
97 103

 Explanation 
Seriously? Just look at the numbers. Try Harder. Again look at the numbers.

SAMPLE INPUT
12028 12772

SAMPLE OUTPUT
97 103
"""

from math import gcd

def calculate_box_contents(n: int, m: int) -> tuple:
    """
    Calculate the number of apples and oranges in each box such that:
    1. The number of apples in each box is the same.
    2. The number of oranges in each box is the same.
    3. The number of boxes is maximized.

    Parameters:
    - n (int): Number of apples.
    - m (int): Number of oranges.

    Returns:
    - tuple: A tuple containing two integers (apples_per_box, oranges_per_box).
    """
    g = gcd(n, m)
    apples_per_box = n // g
    oranges_per_box = m // g
    return (apples_per_box, oranges_per_box)