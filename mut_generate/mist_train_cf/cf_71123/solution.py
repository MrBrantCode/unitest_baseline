"""
QUESTION:
Develop a function named `transform_text` that takes a string as an argument, transforms the text into uppercase, searches for numerical values, converts them into corresponding English words (considering each digit individually for numbers with two or more digits), handles punctuation correctly, and returns the transformed string.
"""

def transform_text(text):
    digit_to_word = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE"
    }

    words = [digit_to_word[character] if character.isdigit() else character for character in text.upper()]
    return ' '.join(words)  