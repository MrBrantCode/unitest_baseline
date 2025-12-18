"""
QUESTION:
Create a function `analyze_text` that takes a string of Chinese text as input and returns a dictionary containing the counts of Chinese characters, English letters, digits, and special symbols in the text. The function should correctly identify and count the occurrences of these character types in the input text. The counts should be returned as a dictionary with keys "chinese_characters", "english_letters", "digits", and "special_symbols".
"""

import re

def analyze_text(text):
    chinese_count = len(re.findall(r'[\u4e00-\u9fff]', text))
    english_count = len(re.findall(r'[a-zA-Z]', text))
    digit_count = len(re.findall(r'\d', text))
    special_count = len(text) - chinese_count - english_count - digit_count
    return {
        "chinese_characters": chinese_count,
        "english_letters": english_count,
        "digits": digit_count,
        "special_symbols": special_count
    }