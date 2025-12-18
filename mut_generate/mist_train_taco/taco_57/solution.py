"""
QUESTION:
Casimir has a string $s$ which consists of capital Latin letters 'A', 'B', and 'C' only. Each turn he can choose to do one of the two following actions:

he can either erase exactly one letter 'A' and exactly one letter 'B' from arbitrary places of the string (these letters don't have to be adjacent);

or he can erase exactly one letter 'B' and exactly one letter 'C' from arbitrary places in the string (these letters don't have to be adjacent).

Therefore, each turn the length of the string is decreased exactly by $2$. All turns are independent so for each turn, Casimir can choose any of two possible actions.

For example, with $s$ $=$ "ABCABC" he can obtain a string $s$ $=$ "ACBC" in one turn (by erasing the first occurrence of 'B' and the second occurrence of 'A'). There are also many other options for a turn aside from this particular example.

For a given string $s$ determine whether there is a sequence of actions leading to an empty string. In other words, Casimir's goal is to erase all letters from the string. Is there a way to do this?


-----Input-----

The first line contains an integer $t$ ($1 \le t \le 1000$) — the number of test cases.

Each test case is described by one string $s$, for which you need to determine if it can be fully erased by some sequence of turns. The string $s$ consists of capital letters 'A', 'B', 'C' and has a length from $1$ to $50$ letters, inclusive.


-----Output-----

Print $t$ lines, each line containing the answer to the corresponding test case. The answer to a test case should be YES if there is a way to fully erase the corresponding string and NO otherwise.

You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes, and YES will all be recognized as positive answers).


-----Examples-----

Input
6
ABACAB
ABBA
AC
ABC
CABCBB
BCBCBCBCBCBCBCBC
Output
NO
YES
NO
NO
YES
YES


-----Note-----

None
"""

def can_erase_string(s: str) -> bool:
    """
    Determines if the given string s can be fully erased by a sequence of actions.
    Each action can either erase one 'A' and one 'B' or one 'B' and one 'C'.

    Parameters:
    s (str): The input string consisting of 'A', 'B', and 'C'.

    Returns:
    bool: True if the string can be fully erased, False otherwise.
    """
    return s.count('B') == s.count('A') + s.count('C')