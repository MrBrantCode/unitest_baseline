"""
QUESTION:
Peter can see a clock in the mirror from the place he sits in the office.
When he saw the clock shows 12:22



1
2
3
4
5
6
7
8
9
10
11
12




He knows that the time is 11:38



1
2
3
4
5
6
7
8
9
10
11
12




in the same manner:

05:25 --> 06:35

01:50 --> 10:10

11:58 --> 12:02

12:01 --> 11:59

Please complete the function `WhatIsTheTime(timeInMirror)`, where `timeInMirror` is the mirrored time (what Peter sees) as string.

Return the _real_ time as a string.

Consider hours to be between 1 <= hour < 13.

So there is no 00:20, instead it is 12:20.

There is no 13:20, instead it is 01:20.
"""

def real_time_from_mirror(time_in_mirror: str) -> str:
    """
    Converts the mirrored time (what Peter sees) to the real time.

    Parameters:
    time_in_mirror (str): The mirrored time in the format "HH:MM".

    Returns:
    str: The real time in the format "HH:MM".
    """
    h, m = map(int, time_in_mirror.split(':'))
    real_hour = -(h + (m != 0)) % 12 or 12
    real_minute = -m % 60
    return f"{real_hour:02}:{real_minute:02}"