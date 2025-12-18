"""
QUESTION:
Implement the Burrows-Wheeler Transform (BWT) function `bwt(s)` that takes a string `s` as input and returns its transformed result. Also, implement the inverse Burrows-Wheeler Transform function `ibwt(r)` that takes a transformed string `r` as input and returns the original string. The input string `s` can contain any characters, including 'e' to 'z' and is case sensitive. The transformed string should include an end of text marker. The functions should handle all edge cases and restrictions.
"""

def burrows_wheeler_transform(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
    s = s + "\003"  # Add end of text marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string

def inverse_burrows_wheeler_transform(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
    return s.rstrip("\003")  # Get rid of trailing ETX marker