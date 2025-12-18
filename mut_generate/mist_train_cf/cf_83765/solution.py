"""
QUESTION:
Implement the `decode_string` function to decode a given encoded string. The encoded string is in the format `k[encoded_string]`, where `k` is a positive integer and `encoded_string` is a string that can contain lowercase English letters, digits, and square brackets. The encoded string can have up to 3 levels of nesting. Return the decoded string.

Constraints:
- The input string `s` is guaranteed to be valid and does not contain extra white spaces.
- The input string `s` consists of lowercase English letters, digits, and square brackets '[]'.
- The length of the input string `s` is between 1 and 100.
- All integers in `s` are in the range `[1, 300]`.
"""

def decode_string(s):
    stack = []
    cur_num = 0
    cur_str = ''
    
    for char in s:
        if char == '[':
            stack.append(cur_str)
            stack.append(cur_num)
            cur_str = ''
            cur_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            cur_str = prev_str + num * cur_str
        elif char.isdigit():
            cur_num = cur_num * 10 + int(char)
        else:
            cur_str += char
    return cur_str