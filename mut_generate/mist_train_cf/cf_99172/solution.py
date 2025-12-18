"""
QUESTION:
Create a function `text_analysis` that takes a string `text` as input and returns a dictionary with three keys: `num_words`, `vowel_list`, and `vowel_freq`. The function should count the number of words in the text, identify all vowel letters in the text (excluding consonants), and count the frequency of each vowel. The function should be able to handle large texts.
"""

def text_analysis(text):
    # Count the number of words in the text
    num_words = len(text.split())

    # Identify all vowel letters in the text
    vowels = "aeiou"
    vowel_list = [char for char in text.lower() if char in vowels]

    # Count the frequency of each vowel
    vowel_freq = {}
    for vowel in vowel_list:
        if vowel in vowel_freq:
            vowel_freq[vowel] += 1
        else:
            vowel_freq[vowel] = 1

    return {
        "num_words": num_words,
        "vowel_list": vowel_list,
        "vowel_freq": vowel_freq
    }