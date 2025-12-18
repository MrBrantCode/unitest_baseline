"""
QUESTION:
# Task
 Given a string `s`, find out if its characters can be rearranged to form a palindrome.

# Example

 For `s = "aabb"`, the output should be `true`.

 We can rearrange `"aabb"` to make `"abba"`, which is a palindrome.

# Input/Output


 - `[input]` string `s`

    A string consisting of lowercase English letters.

    Constraints:

    `4 ≤ inputString.length ≤ 50.`


 - `[output]` a boolean value

    `true` if the characters of the inputString can be rearranged to form a palindrome, `false` otherwise.
"""

def can_form_palindrome(s: str) -> bool:
    """
    Determines if the characters of the input string can be rearranged to form a palindrome.

    Parameters:
    s (str): A string consisting of lowercase English letters.

    Returns:
    bool: True if the characters can be rearranged to form a palindrome, False otherwise.
    """
    return sum((s.count(c) % 2 for c in set(s))) < 2