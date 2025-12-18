"""
QUESTION:
Write a function `categorize_strings(lst, pattern)` that takes a list of strings `lst` and a pattern string `pattern` as input. Categorize each string in `lst` into one of three categories: "short", "long", or "pattern-matched", based on the following conditions: 

- "short": The length of the string is less than 5 characters.
- "long": The length of the string is equal to or more than 5 characters.
- "pattern-matched": The string contains the provided `pattern` string.

The function should return a dictionary with the keys as categories and values as lists of strings that fall into each category, maintaining their original order. 

Restrictions: 
- `lst` contains alphanumeric strings of length 1 to 10^3, with 1 <= len(lst) <= 10^5.
- `pattern` is a string of length 1 to 10^3.
"""

def categorize_strings(lst, pattern):
    result = {"short": [], "long": [], "pattern-matched": []}
    for s in lst:
        if pattern in s:
            result["pattern-matched"].append(s)
        elif len(s) < 5:
            result["short"].append(s)
        else:
            result["long"].append(s)
    return result