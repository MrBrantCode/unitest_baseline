"""
QUESTION:
Write a program which reads an integer $S$ [second] and converts it to $h:m:s$ where $h$, $m$, $s$ denote hours, minutes (less than 60) and seconds (less than 60) respectively.

Constraints

* $0 \leq S \leq 86400$

Input

An integer $S$ is given in a line.

Output

Print $h$, $m$ and $s$ separated by ':'. You do not need to put '0' for a value, which consists of a digit.

Example

Input

46979


Output

13:2:59
"""

def convert_seconds_to_hms(seconds: int) -> str:
    """
    Converts a given number of seconds into the format h:m:s where h is hours, m is minutes, and s is seconds.

    Parameters:
    seconds (int): The total number of seconds to be converted.

    Returns:
    str: A string in the format "h:m:s".
    """
    a = 60
    hours = seconds // (a ** 2)
    minutes = (seconds // a) % a
    seconds = seconds % a
    return f'{hours}:{minutes}:{seconds}'