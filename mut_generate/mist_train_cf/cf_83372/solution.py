"""
QUESTION:
Write a function `is_reverse_anagram(text)` that determines if a given string of words is an anagram of its reversed form, ignoring spaces and treating uppercase and lowercase letters as identical. The function should return True if the string is an anagram of its reverse, and False otherwise.
"""

def is_reverse_anagram(text):
    filtered_text = text.replace(" ", "").lower()
    return filtered_text == filtered_text[::-1]