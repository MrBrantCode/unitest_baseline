"""
QUESTION:
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".


Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".


Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".


Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:

Can you solve it in O(N) time and O(1) space?
"""

def backspace_compare(S1: str, S2: str) -> bool:
    def get_char(s: str, i: int) -> tuple:
        char = ''
        count = 0
        while i >= 0 and (not char):
            if s[i] == '#':
                count += 1
            elif count == 0:
                char = s[i]
            else:
                count -= 1
            i -= 1
        return (char, i)

    i1 = len(S1) - 1
    i2 = len(S2) - 1
    while i1 >= 0 or i2 >= 0:
        c1 = ''
        c2 = ''
        if i1 >= 0:
            (c1, i1) = get_char(S1, i1)
        if i2 >= 0:
            (c2, i2) = get_char(S2, i2)
        if c1 != c2:
            return False
    return True