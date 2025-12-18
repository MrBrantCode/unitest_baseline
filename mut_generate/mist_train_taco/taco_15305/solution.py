"""
QUESTION:
Given a lowercase Latin character (letter), check if it appears in the string ${codeforces}$.


-----Input-----

The first line of the input contains an integer $t$ ($1 \leq t \leq 26$) — the number of test cases.

The only line of each test case contains a character $c$ — a single lowercase Latin character (letter).


-----Output-----

For each test case, output "YES" (without quotes) if $c$ satisfies the condition, and "NO" (without quotes) otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).


-----Examples-----

Input
10
a
b
c
d
e
f
g
h
i
j
Output
NO
NO
YES
YES
YES
YES
NO
NO
NO
NO


-----Note-----

None
"""

def check_character_in_codeforces(c: str) -> str:
    """
    Check if the given character appears in the string "codeforces".

    Parameters:
    c (str): A single lowercase Latin character (letter) to be checked.

    Returns:
    str: "YES" if the character appears in "codeforces", "NO" otherwise.
    """
    if c in 'codeforces':
        return 'YES'
    else:
        return 'NO'