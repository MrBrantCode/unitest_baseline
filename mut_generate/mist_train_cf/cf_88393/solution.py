"""
QUESTION:
Implement a function `replace_pattern(pattern, text)` that replaces all occurrences of `pattern` with the word "lessons" in `text`, while preserving the original case of the letters in the replaced word. The function should be case-insensitive and not use the built-in `replace()` function. It should have a time complexity of O(n), where n is the length of the input text, and a space complexity of O(1).
"""

def replace_pattern(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    
    result = ""
    i = 0
    
    while i < text_length:
        # Check if there is a match for the pattern starting at index i
        if text[i:i+pattern_length].lower() == pattern.lower():
            # Replace the pattern with "lessons" while preserving the original case
            result += "Lessons" if text[i].isupper() else "lessons"
            i += pattern_length
        else:
            # If no match, add the current character to the result and move to the next character
            result += text[i]
            i += 1
    
    return result