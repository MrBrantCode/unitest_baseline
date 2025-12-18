"""
QUESTION:
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.




Note: You may assume the string contain only lowercase letters.
"""

def find_first_non_repeating_char_index(s: str) -> int:
    if not s:
        return -1
    elif len(s) == 1:
        return 0
    
    result = len(s)
    
    for ch in range(ord('a'), ord('z') + 1):
        char = chr(ch)
        if s.find(char) == -1:
            continue
        if s.find(char) == s.rfind(char):
            result = min(result, s.find(char))
    
    return result if result < len(s) else -1