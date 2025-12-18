"""
QUESTION:
A magic number is a number formed by concatenation of numbers 1, 14 and 144. We can use each of these numbers any number of times. Therefore 14144, 141414 and 1411 are magic numbers but 1444, 514 and 414 are not.

You're given a number. Determine if it is a magic number or not.


-----Input-----

The first line of input contains an integer n, (1 ≤ n ≤ 10^9). This number doesn't contain leading zeros.


-----Output-----

Print "YES" if n is a magic number or print "NO" if it's not.


-----Examples-----
Input
114114

Output
YES

Input
1111

Output
YES

Input
441231

Output
NO
"""

import re

def is_magic_number(n: int) -> str:
    """
    Determines if a given number is a magic number.

    A magic number is a number formed by concatenation of numbers 1, 14, and 144.
    Each of these numbers can be used any number of times.

    Parameters:
    n (int): The number to be checked.

    Returns:
    str: "YES" if the number is a magic number, "NO" otherwise.
    """
    # Convert the integer to a string for pattern matching
    n_str = str(n)
    
    # Use regular expression to check if the number matches the pattern
    if re.match(r'^(14?4?)*$', n_str):
        return "YES"
    else:
        return "NO"