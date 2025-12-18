"""
QUESTION:
Implement a function named `replace_string(text, old, new)` that replaces every occurrence of the string `old` in the string `text` with the string `new`, preserving the original case of the letters. The function should handle multiple occurrences of `old` in `text`, and both `old` and `new` can be of any length and may contain special characters. Additionally, the function should handle cases where `old` is an empty string or `new` is an empty string.
"""

def replace_string(text, old, new):
    if old == "":
        return text.replace(old, new)
    
    result = ""
    i = 0
    
    while i < len(text):
        if text[i:i+len(old)].lower() == old.lower():
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    
    return result