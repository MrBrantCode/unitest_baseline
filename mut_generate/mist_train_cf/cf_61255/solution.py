"""
QUESTION:
Design a function `unique_char_info` that takes a string `s` as input. The function should find the first non-repeating character in `s`, return its index position, ASCII value, and base64 encoded string. If all characters in `s` repeat, return "No unique character found." The function should treat uppercase and lowercase letters as distinct characters due to their different ASCII values.
"""

import base64

def unique_char_info(s):
    count_dict = {}
    for i in range(len(s)):
        if s[i] not in count_dict:
            count_dict[s[i]] = [i, 1]
        else:
            count_dict[s[i]][1] += 1

    for item in count_dict:
        if count_dict[item][1] == 1:
            ascii_val = ord(item)
            base64_str = base64.b64encode(item.encode()).decode('utf-8')
            return {'Index': count_dict[item][0], 'ASCII': ascii_val, 'Base64': base64_str}

    return("No unique character found.")