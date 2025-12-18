"""
QUESTION:
Write a function `capitalize_target_word(text, target)` that takes a block of text and a target word as input. The function should return the modified text with all occurrences of the target word changed to uppercase. The function should only change the casing of the target word when it appears as a whole word, not when it appears as part of another word. The function should not use any built-in string functions.
"""

def capitalize_target_word(text, target):
    result = ""
    words = text.split()
    
    for word in words:
        if word == target:
            result += word.upper() + " "
        else:
            result += word + " "
    return result.rstrip()