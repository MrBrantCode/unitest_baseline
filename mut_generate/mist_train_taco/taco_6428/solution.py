"""
QUESTION:
Your task is to write an update for a lottery machine. Its current version produces a sequence of random letters and integers (passed as a string to the function). Your code must filter out all letters and return **unique** integers as a string, in their order of first appearance. If there are no integers in the string return `"One more run!"`

## Examples

```
"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"
```
"""

def extract_unique_integers_from_string(s: str) -> str:
    # Filter out all letters and keep only digits
    digits = filter(str.isdigit, s)
    # Use a dictionary to keep unique digits in order of first appearance
    unique_digits = ''.join(dict.fromkeys(digits))
    # Return the result or "One more run!" if no digits are found
    return unique_digits or "One more run!"