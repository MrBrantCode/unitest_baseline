"""
QUESTION:
You are given a 4-character string S consisting of uppercase English letters.
Determine if S consists of exactly two kinds of characters which both appear twice in S.

-----Constraints-----
 - The length of S is 4.
 - S consists of uppercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
If S consists of exactly two kinds of characters which both appear twice in S, print Yes; otherwise, print No.

-----Sample Input-----
ASSA

-----Sample Output-----
Yes

S consists of A and S which both appear twice in S.
"""

def check_two_characters_twice(S: str) -> str:
    # Ensure the input string has exactly 4 characters
    if len(S) != 4:
        raise ValueError("Input string must be exactly 4 characters long.")
    
    # Count the frequency of each character
    char_count = {}
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check if there are exactly two characters each appearing twice
    if len(char_count) == 2 and all(count == 2 for count in char_count.values()):
        return 'Yes'
    else:
        return 'No'