"""
QUESTION:
[Image] 


-----Input-----

The input contains a single integer $a$ ($0 \le a \le 15$).


-----Output-----

Output a single integer.


-----Example-----
Input
3

Output
13
"""

def transform_integer(a: int) -> int:
    ans = [15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7]
    return ans[a]