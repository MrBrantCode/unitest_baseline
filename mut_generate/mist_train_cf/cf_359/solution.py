"""
QUESTION:
Write a function `reverse_alphanumeric_text(text)` that takes an input string `text` of up to 1000 characters and returns the string with alphanumeric characters reversed character by character, ignoring non-alphanumeric characters and maintaining the original capitalization.
"""

def reverse_alphanumeric_text(text):
    original_text = list(text)
    left, right = 0, len(text) - 1

    while left < right:
        if not original_text[left].isalnum():
            left += 1
        elif not original_text[right].isalnum():
            right -= 1
        else:
            original_text[left], original_text[right] = original_text[right], original_text[left]
            left += 1
            right -= 1

    return ''.join(original_text)