"""
QUESTION:
There is a string s of length 3 or greater. No two neighboring characters in s are equal.

Takahashi and Aoki will play a game against each other. The two players alternately performs the following operation, Takahashi going first:

* Remove one of the characters in s, excluding both ends. However, a character cannot be removed if removal of the character would result in two neighboring equal characters in s.



The player who becomes unable to perform the operation, loses the game. Determine which player will win when the two play optimally.

Constraints

* 3 ≤ |s| ≤ 10^5
* s consists of lowercase English letters.
* No two neighboring characters in s are equal.

Input

The input is given from Standard Input in the following format:


s


Output

If Takahashi will win, print `First`. If Aoki will win, print `Second`.

Examples

Input

aba


Output

Second


Input

abc


Output

First


Input

abcab


Output

First
"""

def determine_winner(s: str) -> str:
    if s[0] == s[-1]:
        if len(s) % 2 == 0:
            return 'First'
        else:
            return 'Second'
    elif len(s) % 2 == 0:
        return 'Second'
    else:
        return 'First'