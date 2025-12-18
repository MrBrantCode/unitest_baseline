"""
QUESTION:
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 
Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

 
Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""

def remove_adjacent_duplicates(S: str) -> str:
    from string import ascii_lowercase
    
    # Create a set of all possible adjacent duplicate pairs
    dup = {2 * ch for ch in ascii_lowercase}
    
    prev_length = -1
    while prev_length != len(S):
        prev_length = len(S)
        for d in dup:
            S = S.replace(d, '')
    
    return S