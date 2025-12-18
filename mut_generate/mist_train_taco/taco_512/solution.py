"""
QUESTION:
There is a string s of length 3 or greater.
No two neighboring characters in s are equal.
Takahashi and Aoki will play a game against each other.
The two players alternately performs the following operation, Takahashi going first:
 - Remove one of the characters in s, excluding both ends. However, a character cannot be removed if removal of the character would result in two neighboring equal characters in s.
The player who becomes unable to perform the operation, loses the game. Determine which player will win when the two play optimally.

-----Constraints-----
 - 3 ≤ |s| ≤ 10^5
 - s consists of lowercase English letters.
 - No two neighboring characters in s are equal.

-----Input-----
The input is given from Standard Input in the following format:
s

-----Output-----
If Takahashi will win, print First. If Aoki will win, print Second.

-----Sample Input-----
aba

-----Sample Output-----
Second

Takahashi, who goes first, cannot perform the operation, since removal of the b, which is the only character not at either ends of s, would result in s becoming aa, with two as neighboring.
"""

def determine_winner(s: str) -> str:
    """
    Determines the winner of the game between Takahashi and Aoki.

    The game involves alternately removing characters from the string `s`, excluding both ends,
    with the condition that a character cannot be removed if it would result in two neighboring
    equal characters. The player who cannot perform the operation loses.

    Args:
        s (str): The input string with length 3 or greater, consisting of lowercase English letters,
                 and no two neighboring characters being equal.

    Returns:
        str: "First" if Takahashi wins, "Second" if Aoki wins.
    """
    return ['Second', 'First'][len(s.rstrip(s[0])) % 2]