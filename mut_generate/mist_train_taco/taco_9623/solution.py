"""
QUESTION:
A string is said to be complete if it contains all the characters from a to z. Given a string, check if it complete or not.

Input
First line of the input contains the number of strings N. It is followed by N lines each contains a single string.

Output
For each test case print "YES" if the string is complete, else print "NO"

Constraints
1 ≤ N ≤ 10
The length of the string is at max 100 and the string contains only the characters a to z

SAMPLE INPUT
3
wyyga
qwertyuioplkjhgfdsazxcvbnm
ejuxggfsts

SAMPLE OUTPUT
NO
YES
NO
"""

def is_complete_string(s: str) -> str:
    # List of all characters from 'a' to 'z'
    all_chars = [chr(i) for i in range(97, 123)]
    
    # Check if each character from 'a' to 'z' is in the string
    for char in all_chars:
        if char not in s:
            return "NO"
    
    return "YES"