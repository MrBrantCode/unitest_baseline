"""
QUESTION:
Implement a function called `replace_pattern_with_lessons` that takes two strings, `pattern` and `text`, and replaces all occurrences of `pattern` in `text` with the word "lessons" in a case-insensitive manner. The function should preserve the original case of the letters in the replaced word "lessons". The function should not use the built-in `replace()` function.
"""

def replace_pattern_with_lessons(pattern, text):
    result = ""
    pattern_lower = pattern.lower()
    i = 0
    
    while i < len(text):
        if text[i:i+len(pattern)].lower() == pattern_lower:
            if text[i].isupper():
                result += "LESSONS"
            elif text[i].islower():
                result += "lessons"
            else:
                result += "Lessons"
            i += len(pattern)
        else:
            result += text[i]
            i += 1
    
    return result