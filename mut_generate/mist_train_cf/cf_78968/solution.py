"""
QUESTION:
Implement two functions, `bwt(s)` and `ibwt(r)`, that perform the Burrows-Wheeler Transform and its inverse on a given string `s` and transformed string `r`, respectively. The functions should exclude inputs that contain the special characters STX (`\002`) and ETX (`\003`). The `bwt(s)` function should append an ETX character to the end of the input string `s` before performing the transformation.
"""

def burrows_wheeler_transform(s):
    assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
    s = s + "\003"  # Add end of text character
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string


def inverse_burrows_wheeler_transform(r):
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
    return s.rstrip("\003")  # Get rid of trailing ETX character