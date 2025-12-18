"""
QUESTION:
Create a function named `extract_substring(s, pos1, pos2)` that takes a string `s` and two integer positions `pos1` and `pos2` as input, and returns the substring of `s` between `pos1` and `pos2` (exclusive). Ensure that `pos1` and `pos2` are integers, `pos1` is less than or equal to `pos2`, and both positions are within the length of the string `s`. If any of these conditions are not met, return a custom error message.
"""

def extract_substring(s, pos1, pos2):
    try:
        if pos1 > pos2:
            return "Error: Second position should be greater than the first position."
        elif pos1 > len(s) or pos2 > len(s):
            return "Error: Given positions exceeded the length of the string."
        else:
            return s[pos1:pos2]
    except TypeError:
        return "Error: Both positions should be integers."