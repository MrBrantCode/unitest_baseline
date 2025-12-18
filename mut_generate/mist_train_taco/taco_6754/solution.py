"""
QUESTION:
-----Input-----

The input consists of a single string of uppercase letters A-Z. The length of the string is between 1 and 10 characters, inclusive.


-----Output-----

Output "YES" or "NO".


-----Examples-----
Input
NEAT

Output
YES

Input
WORD

Output
NO

Input
CODER

Output
NO

Input
APRILFOOL

Output
NO

Input
AI

Output
YES

Input
JUROR

Output
YES

Input
YES

Output
NO
"""

def check_string_pattern(s: str) -> str:
    curved = 'QRUOPJGDSCB'
    ctr = 0
    for char in s:
        if char in curved:
            ctr += 1
    if ctr == 0 or ctr == len(s):
        return 'YES'
    else:
        return 'NO'