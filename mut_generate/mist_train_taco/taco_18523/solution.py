"""
QUESTION:
## Task

Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.

## Example

For the input `cdcab`, the output should be `bacdcab`

## Input/Output

Input is a string consisting of lowercase latin letters with length 3 <= str.length <= 10

The output is a palindrome string satisfying the task.

For s = `ab` either solution (`aba` or `bab`) will be accepted.
"""

def make_palindrome(s: str) -> str:
    for n in range(len(s), -1, -1):
        if s[:n] == s[:n][::-1]:
            return s[n:][::-1] + s
        if s[-n:] == s[-n:][::-1]:
            return s + s[:-n][::-1]