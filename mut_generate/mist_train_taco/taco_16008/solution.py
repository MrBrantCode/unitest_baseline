"""
QUESTION:
_Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year._

Find the number of Friday 13th in the given year.

__Input:__ Year as an integer.

__Output:__ Number of Black Fridays in the year as an integer.

__Examples:__

        unluckyDays(2015) == 3
        unluckyDays(1986) == 1

***Note:*** In Ruby years will start from 1593.
"""

from datetime import date

def count_unlucky_days(year: int) -> int:
    """
    Counts the number of Friday the 13ths in the given year.

    Parameters:
    year (int): The year to check for Friday the 13ths.

    Returns:
    int: The number of Friday the 13ths in the given year.
    """
    return sum((date(year, m, 13).weekday() == 4 for m in range(1, 13)))