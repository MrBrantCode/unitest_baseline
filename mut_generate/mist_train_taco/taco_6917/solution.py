"""
QUESTION:
Given is a string S representing the day of the week today.
S is SUN, MON, TUE, WED, THU, FRI, or SAT, for Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively.
After how many days is the next Sunday (tomorrow or later)?

-----Constraints-----
 - S is SUN, MON, TUE, WED, THU, FRI, or SAT.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the number of days before the next Sunday.

-----Sample Input-----
SAT

-----Sample Output-----
1

It is Saturday today, and tomorrow will be Sunday.
"""

def days_until_next_sunday(S: str) -> int:
    """
    Calculate the number of days until the next Sunday from the given day of the week.

    Parameters:
    S (str): The current day of the week, which should be one of "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT".

    Returns:
    int: The number of days until the next Sunday.
    """
    days_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    current_day_index = days_of_week.index(S)
    return 7 - current_day_index