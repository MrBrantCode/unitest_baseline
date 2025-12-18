"""
QUESTION:
Write a function that receives two strings as parameter. This strings are in the following format of date: `YYYY/MM/DD`.
Your job is: Take the `years` and calculate the difference between them.

Examples:
```
'1997/10/10' and '2015/10/10' -> 2015 - 1997 = returns 18 
'2015/10/10' and '1997/10/10' -> 2015 - 1997 = returns 18
```
At this level, you don't need validate months and days to calculate the difference.
"""

def calculate_year_difference(date1: str, date2: str) -> int:
    """
    Calculate the absolute difference in years between two dates given in the format 'YYYY/MM/DD'.

    Parameters:
    date1 (str): The first date in the format 'YYYY/MM/DD'.
    date2 (str): The second date in the format 'YYYY/MM/DD'.

    Returns:
    int: The absolute difference in years between the two dates.
    """
    year1 = int(date1.split('/')[0])
    year2 = int(date2.split('/')[0])
    return abs(year1 - year2)