"""
QUESTION:
Implement a function `decodeString` that takes a string `s` as input and returns the decoded string. The input string `s` is encoded in a specific format where some substrings are repeated multiple times using the rule `k[encoded_string]`, where `k` is a positive integer and `encoded_string` is repeated exactly `k` times. Assume the input string `s` is non-empty and does not contain extra leading, trailing spaces, or square brackets within the encoded string.
"""

def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append(current_str)
            stack.append(current_num)
            current_str = ''
            current_num = 0
        elif char == ']':
            num = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
    
    return current_str