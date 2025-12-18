"""
QUESTION:
You are given the current time in 24-hour format hh:mm. Find and print the time after a minutes.

Note that you should find only the time after a minutes, see the examples to clarify the problem statement.

You can read more about 24-hour format here https://en.wikipedia.org/wiki/24-hour_clock.


-----Input-----

The first line contains the current time in the format hh:mm (0 ≤ hh < 24, 0 ≤ mm < 60). The hours and the minutes are given with two digits (the hours or the minutes less than 10 are given with the leading zeroes).

The second line contains integer a (0 ≤ a ≤ 10^4) — the number of the minutes passed.


-----Output-----

The only line should contain the time after a minutes in the format described in the input. Note that you should print exactly two digits for the hours and the minutes (add leading zeroes to the numbers if needed).

See the examples to check the input/output format.


-----Examples-----
Input
23:59
10

Output
00:09

Input
20:20
121

Output
22:21

Input
10:10
0

Output
10:10
"""

def calculate_time_after_minutes(current_time: str, minutes_to_add: int) -> str:
    # Split the current time into hours and minutes
    hh, mm = map(int, current_time.split(':'))
    
    # Add the minutes to the current time
    mm += minutes_to_add
    
    # Handle the overflow of minutes
    while mm >= 60:
        hh += 1
        mm -= 60
    
    # Handle the overflow of hours
    while hh >= 24:
        hh -= 24
    
    # Format the hours and minutes to ensure two digits
    new_time = f'{hh:02}:{mm:02}'
    
    return new_time