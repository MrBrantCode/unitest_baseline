"""
QUESTION:
Dolphin loves programming contests. Today, he will take part in a contest in AtCoder.

In this country, 24-hour clock is used. For example, 9:00 p.m. is referred to as "21 o'clock".

The current time is A o'clock, and a contest will begin in exactly B hours.
When will the contest begin? Answer in 24-hour time.

-----Constraints-----
 - 0 \leq A,B \leq 23
 - A and B are integers.

-----Input-----
The input is given from Standard Input in the following format:
A B

-----Output-----
Print the hour of the starting time of the contest in 24-hour time.

-----Sample Input-----
9 12

-----Sample Output-----
21

In this input, the current time is 9 o'clock, and 12 hours later it will be 21 o'clock in 24-hour time.
"""

def calculate_contest_start_time(A: int, B: int) -> int:
    """
    Calculate the hour of the contest start time in 24-hour format.

    Parameters:
    - A (int): The current hour in 24-hour format.
    - B (int): The number of hours until the contest starts.

    Returns:
    - int: The hour of the contest start time in 24-hour format.
    """
    return (A + B) % 24