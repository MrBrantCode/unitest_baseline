"""
QUESTION:
The numbers of all offices in the new building of the Tax Office of IT City will have lucky numbers.

Lucky number is a number that consists of digits 7 and 8 only. Find the maximum number of offices in the new building of the Tax Office given that a door-plate can hold a number not longer than n digits.


-----Input-----

The only line of input contains one integer n (1 ≤ n ≤ 55) — the maximum length of a number that a door-plate can hold.


-----Output-----

Output one integer — the maximum number of offices, than can have unique lucky numbers not longer than n digits.


-----Examples-----
Input
2

Output
6
"""

def calculate_max_offices(n: int) -> int:
    """
    Calculate the maximum number of offices that can have unique lucky numbers not longer than n digits.

    :param n: The maximum length of a number that a door-plate can hold (1 ≤ n ≤ 55).
    :return: The maximum number of offices with unique lucky numbers.
    """
    return pow(2, n + 1) - 2