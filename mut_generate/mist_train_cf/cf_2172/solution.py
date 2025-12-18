"""
QUESTION:
Write a function `count_vowels` that takes a string `text` and an integer `vowel_count` as input parameters. The function should recursively remove all occurrences of the word "the" from the text while ignoring case sensitivity, and not removing the word "the" if it's part of another word. The function should then calculate the total number of vowels (a, e, i, o, u) in the modified text and return the count.
"""

def count_vowels(text, vowel_count):
    if "the" in text.lower():
        text = text.lower().replace("the", "")
        return count_vowels(text, vowel_count)
    elif len(text) == 0:
        return vowel_count
    else:
        if text[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        return count_vowels(text[1:], vowel_count)