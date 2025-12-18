"""
QUESTION:
# Story

Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly. 

Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!

What a bunch of cheapskates!

Can you do it?

# Kata

Given the ```angle``` (in degrees) of the hour-hand, return the time in HH:MM format. Round _down_ to the nearest minute.

# Examples

* ```12:00``` = 0 degrees


* ```03:00``` = 90 degrees


* ```06:00``` = 180 degrees


* ```09:00``` = 270 degrees


* ```12:00``` = 360 degrees

# Notes

* 0 <= ```angle``` <= 360
"""

def get_time_from_angle(angle: float) -> str:
    """
    Given the angle (in degrees) of the hour-hand, return the time in HH:MM format.
    The time is rounded down to the nearest minute.

    Parameters:
    - angle (float): The angle of the hour-hand in degrees.

    Returns:
    - str: The time in HH:MM format.
    """
    hr = int(angle // 30)
    mn = int(angle % 30 * 2)
    if hr == 0:
        hr = 12
    return '{:02d}:{:02d}'.format(hr, mn)