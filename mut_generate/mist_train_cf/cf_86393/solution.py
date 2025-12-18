"""
QUESTION:
Write a function `reverse_alphanumeric_text(text)` that takes an input string `text` of maximum length 1000 characters and returns the reversed text, considering only alphanumeric characters and ignoring any punctuation or special characters. The reversed text should maintain the same capitalization as the original text.
"""

def reverse_alphanumeric_text(text):
    original_text = text
    reversed_text = ""
    text = ''.join(char for char in text if char.isalnum())
    for char in reversed(text):
        reversed_text += char
    result = ""
    j = 0
    for i in range(len(original_text)):
        if original_text[i].isalnum():
            result += reversed_text[j]
            j += 1
        else:
            result += original_text[i]
    return result