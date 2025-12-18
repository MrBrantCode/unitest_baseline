"""
QUESTION:
Implement the function `decodeString(s: str) -> str` to decode a given string `s` that is encoded in a specific format. The encoding format uses a combination of letters and numbers to represent a repeating pattern within the string, where a number represents the number of times the subsequent substring should be repeated, and a pair of square brackets `[]` encloses the substring that needs to be repeated. The function should return the decoded string. 

The input string `s` is guaranteed to be a valid encoded string. The function should be able to handle nested brackets and any combination of letters and numbers.
"""

def decodeString(s: str) -> str:
    stack = []
    curr_num = 0
    curr_str = ''
    
    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c.isalpha():
            curr_str += c
        elif c == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ''
            curr_num = 0
        elif c == ']':
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str
    return curr_str