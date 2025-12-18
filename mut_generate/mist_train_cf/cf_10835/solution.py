"""
QUESTION:
Create a function `capitalize_sentence(sentence)` that takes a sentence as input and returns the formatted sentence. The function should capitalize the first letter of each word. If the sentence starts with a number or special character, the first letter of the first word should still be capitalized. The function should also handle sentences that end with a period, exclamation mark, or question mark and capitalize the first letter of the next word after these punctuation marks, and handle multiple spaces between words by considering consecutive letters as part of a word.
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