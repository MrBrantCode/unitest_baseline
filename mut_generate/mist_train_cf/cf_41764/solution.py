"""
QUESTION:
Write a function `removeSubstring` that takes two parameters: `original` (the original string) and `substring` (the substring to be removed), and returns the modified string with all occurrences of the substring removed.
"""

def entance(original: str, substring: str) -> str:
    return original.replace(substring, "")