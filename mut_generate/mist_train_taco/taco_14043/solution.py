"""
QUESTION:
Your friend who lives in undisclosed country is involved in debt. He is borrowing 100,000-yen from a loan shark. The loan shark adds 5% interest of the debt and rounds it to the nearest 1,000 above week by week.

Write a program which computes the amount of the debt in n weeks.



Input

An integer n (0 ≤ n ≤ 100) is given in a line.

Output

Print the amout of the debt in a line.

Example

Input

5


Output

130000
"""

import math

def calculate_debt_after_n_weeks(n: int) -> int:
    a = 100000
    for _ in range(n):
        a *= 1.05
        a = 1000 * math.ceil(a / 1000)
    return a