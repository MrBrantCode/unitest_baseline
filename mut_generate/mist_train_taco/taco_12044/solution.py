"""
QUESTION:
A string of length 6 consisting of lowercase English letters is said to be coffee-like if and only if its 3-rd and 4-th characters are equal and its 5-th and 6-th characters are also equal.

Given a string S, determine whether it is coffee-like.

-----Constraints-----
 - S is a string of length 6 consisting of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
If S is coffee-like, print Yes; otherwise, print No.

-----Sample Input-----
sippuu

-----Sample Output-----
Yes

In sippuu, the 3-rd and 4-th characters are equal, and the 5-th and 6-th characters are also equal.
"""

def is_coffee_like(s: str) -> str:
    # Check if the string length is 6
    if len(s) != 6:
        return 'No'
    
    # Check if the 3rd and 4th characters are equal
    if s[2] == s[3]:
        # Check if the 5th and 6th characters are equal
        if s[4] == s[5]:
            return 'Yes'
    
    return 'No'