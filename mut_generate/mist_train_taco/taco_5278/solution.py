"""
QUESTION:
# Task
 Given a string `str`, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Example

 For `str = "abcdc"`, the output should be `"abcdcba"`.

# Input/Output


 - `[input]` string `str`

    A string consisting of lowercase latin letters.

    Constraints: `3 ≤ str.length ≤ 10`.


 - `[output]` a string
"""

def make_shortest_palindrome(strng: str) -> str:
    n = 0
    while strng[n:] != strng[n:][::-1]:
        n += 1
    return strng + strng[:n][::-1]