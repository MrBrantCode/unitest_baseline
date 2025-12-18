"""
QUESTION:
# Task
 If string has more than one neighboring dashes(e.g. --) replace they with one dash(-). 
 
 Dashes are considered neighbors even if there is some whitespace **between** them.

# Example

 For `str = "we-are- - - code----warriors.-"`
 
 The result should be `"we-are- code-warriors.-"`
 
# Input/Output


 - `[input]` string `str`
 
 
 - `[output]` a string
"""

import re

def replace_dashes_as_one(s: str) -> str:
    """
    Replaces multiple neighboring dashes (including those with whitespace in between) with a single dash.

    Args:
        s (str): The input string to be processed.

    Returns:
        str: The processed string with multiple neighboring dashes replaced by a single dash.
    """
    return re.sub('-[ -]+-|-+', '-', s)