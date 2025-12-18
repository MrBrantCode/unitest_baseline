"""
QUESTION:
# Task
Given an initial string `s`, switch case of the minimal possible number of letters to make the whole string written in the upper case or in the lower case.

# Input/Output


`[input]` string `s`

String of odd length consisting of English letters.

3 ≤ inputString.length ≤ 99.

`[output]` a string

The resulting string.

# Example

For `s = "Aba"`, the output should be `"aba"`

For `s = "ABa"`, the output should be `"ABA"`
"""

def case_unification(s: str) -> str:
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())
    
    if lower_count > upper_count:
        return s.lower()
    else:
        return s.upper()