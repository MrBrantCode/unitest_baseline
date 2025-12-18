"""
QUESTION:
Create a function `capitalize_sentence(sentence)` that takes a sentence as an argument. The function should return the formatted sentence where the first letter of each word is capitalized. The function should handle cases where the sentence starts with a number or special character, and it should also handle sentences that end with a period, exclamation mark, or question mark by capitalizing the first letter of the next word after any of these punctuation marks. The function should consider consecutive letters as part of a word, ignoring multiple spaces between words.
"""

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0:
            capitalized_words.append(word.capitalize())
        elif word[-1] in ['.', '!', '?']:
            capitalized_words.append(word[:-1].capitalize() + word[-1])
        else:
            capitalized_words.append(word.capitalize())
    return ' '.join(capitalized_words)