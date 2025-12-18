"""
QUESTION:
Write a function `replace_python(text)` that takes a string `text` as an argument. The function should check if the string contains the word "Python" in a case-insensitive manner. If the string contains the word "Python", the function should return the string with all occurrences of "Python" (regardless of case) replaced with the word "Programming". If the string does not contain the word "Python", the function should return the original string.
"""

def replace_python(text):
    if "python" not in text.lower():
        return text
    else:
        return text.replace("Python", "Programming", -1)