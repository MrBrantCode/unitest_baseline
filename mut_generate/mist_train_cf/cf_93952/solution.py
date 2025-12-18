"""
QUESTION:
Implement a function `replace_string(text, old, new)` that replaces every occurrence of the `old` string in the given `text` string with the `new` string, while preserving the original case of the letters. The function should handle multiple occurrences of the `old` string, and it should also work when the `old` string is an empty string or the `new` string is an empty string. The `old` and `new` strings can be of any length and may contain special characters.
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