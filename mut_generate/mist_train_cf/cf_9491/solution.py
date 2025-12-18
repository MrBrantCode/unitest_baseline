"""
QUESTION:
Implement a function `replace_string(text, old, new)` that replaces every occurrence of `old` in `text` with `new`, preserving the original case of the letters. The function should handle multiple occurrences of `old` in `text`. Assume that `text`, `old`, and `new` are non-empty strings.
"""

def replace_string(text, old, new):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old)].lower() == old.lower():
            if text[i].isupper() and new[0].islower():
                result += new.capitalize()
            elif text[i].islower() and new[0].isupper():
                result += new.lower()
            else:
                result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result